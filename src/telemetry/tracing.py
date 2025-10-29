# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Tracing configuration and setup."""

import logging

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc import trace_exporter as trace_exporter_grpc
from opentelemetry.exporter.otlp.proto.http import trace_exporter as trace_exporter_http
from opentelemetry.instrumentation.langchain import LangchainInstrumentor
from opentelemetry.sdk import resources
from opentelemetry.sdk import trace as sdk_trace
from opentelemetry.sdk.trace import export as trace_export

import exceptions

from .providers.factory import create_otel_provider

logger = logging.getLogger(__name__)


def setup_tracing_with_provider(
    provider_name: str,
    protocol: str = None,
    resource: resources.Resource = None,
    **provider_kwargs,
) -> trace.Tracer:
    """Configure and initialize OpenTelemetry tracing with a provider.

    Args:
        provider: OTel provider instance or provider name
        protocol: Protocol to use (http or grpc)
        resource: OpenTelemetry resource
        **provider_kwargs: Additional arguments for provider creation
    """
    LangchainInstrumentor().instrument()

    # Create provider instance if string is passed
    # if isinstance(provider, str):
    provider = create_otel_provider(provider_name, **provider_kwargs)

    endpoint = provider.get_endpoint()
    headers = provider.get_headers()

    logger.info(f"Setup OpenTelemetry Tracer with {provider.name}: {endpoint} ({protocol})")

    # Create span exporter based on protocol
    if protocol == "http":
        # For HTTP, append /v1/traces to the endpoint
        traces_endpoint = f"{endpoint}/v1/traces"
        otlp_span_exporter = trace_exporter_http.OTLPSpanExporter(
            endpoint=traces_endpoint,
            headers=headers,
            compression=trace_exporter_http.Compression.Gzip,
        )
    elif protocol == "grpc":
        otlp_span_exporter = trace_exporter_grpc.OTLPSpanExporter(
            endpoint=endpoint,
            headers=headers,
            insecure=False,  # Use secure connection by default
        )
    else:
        raise exceptions.OpenTelemetryProtocolError(f"invalid OpenTelemetry protocol: {protocol}")

    logger.info(f"OTLP tracing configured for {provider.name}: {endpoint}")

    tracer_provider = sdk_trace.TracerProvider(
        resource=resource,
        span_limits=sdk_trace.SpanLimits(max_attributes=100_000),
    )

    otlp_span_processor = trace_export.BatchSpanProcessor(otlp_span_exporter)
    tracer_provider.add_span_processor(otlp_span_processor)

    trace.set_tracer_provider(tracer_provider)
    logger.info("OpenTelemetry tracing initialized")

    return trace.get_tracer(resource.attributes.get(resources.SERVICE_NAME, "unknown") if resource else "unknown")


# Backward compatibility function
def setup_tracing(
    otlp_endpoint: str,
    otlp_protocol: str,
    resource: resources.Resource,
) -> trace.Tracer:
    """Legacy function for backward compatibility."""
    logger.warning("setup_tracing is deprecated. Use setup_tracing_with_provider instead.")

    # Try to determine provider from endpoint
    if "langchain.com" in otlp_endpoint or "smith.langchain" in otlp_endpoint:
        provider = create_otel_provider("langsmith")
    else:
        # Fallback to a basic configuration
        raise ValueError("Cannot determine provider from endpoint. Use setup_tracing_with_provider instead.")

    return setup_tracing_with_provider(provider, otlp_protocol, resource)


def cleanup_tracing():
    """Clean up tracing instrumentation."""
    LangchainInstrumentor().uninstrument()
