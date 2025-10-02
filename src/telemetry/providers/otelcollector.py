# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""OpenTelemetry Collector provider."""

from os import environ
from typing import Dict, Optional

from .base import OTelProvider


OTEL_COLLECTOR_GRPC_ENDPOINT = "http://localhost:4317"
OTEL_COLLECTOR_HTTP_ENDPOINT = "http://localhost:4318"


class OTelCollectorProvider(OTelProvider):
    """OpenTelemetry Collector provider implementation."""

    def __init__(
        self,
        protocol: Optional[str] = None,
    ):
        """Initialize OpenTelemetry Collector provider.

        Args:
            protocol: Protocol to use - http or grpc (defaults to env OTEL_EXPORTER_OTLP_PROTOCOL)
        """
        self.protocol = protocol or environ.get("OTEL_EXPORTER_OTLP_PROTOCOL", "grpc")
        if self.protocol == "http":
            endpoint = OTEL_COLLECTOR_HTTP_ENDPOINT
        else:
            endpoint = OTEL_COLLECTOR_GRPC_ENDPOINT
        self.endpoint = endpoint
        self.headers = {}
        print(
            f"OpenTelemetry Collector provider setup done - {self.protocol}://{self.endpoint}"
        )

    def get_endpoint(self) -> str:
        """Get the OpenTelemetry Collector endpoint."""
        return self.endpoint

    def get_headers(self) -> Dict[str, str]:
        """Get custom headers for the collector."""
        return self.headers

    def get_project_name(self) -> Optional[str]:
        """Get project name from service name resource attribute."""
        return environ.get("OTEL_SERVICE_NAME", "ai-llm-lab")

    @property
    def name(self) -> str:
        """Get the provider name."""
        return "otelcollector"

    def is_insecure(self) -> bool:
        """Check if connection should be insecure."""
        return self.insecure

    def get_protocol(self) -> str:
        """Get the protocol being used."""
        return self.protocol
