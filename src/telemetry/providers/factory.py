# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Factory for creating OpenTelemetry providers."""

from enum import Enum
from typing import Any

from .agenta import AgentaProvider
from .base import OTelProvider
from .braintrust import BrainTrustProvider
from .laminar import LaminarProvider
from .langfuse import LangfuseProvider
from .langsmith import LangsmithProvider
from .otelcollector import OTelCollectorProvider
from .traceloop import TraceloopProvider
from exceptions import OpenTelemetryProviderException


class OTelProviderType(Enum):
    """Supported OpenTelemetry provider types."""

    LANGSMITH = "langsmith"
    AGENTA = "agenta"
    LANGFUSE = "langfuse"
    TRACELOOP = "traceloop"
    BRAINTRUST = "braintrust"
    LAMINAR = "laminar"
    OTELCOLLECTOR = "otelcollector"


def create_otel_provider(provider_name: str, **kwargs: Any) -> OTelProvider:
    """Create an OpenTelemetry provider instance.

    Args:
        provider: The provider type (langsmith or agenta)
        **kwargs: Provider-specific configuration arguments

    Returns:
        Configured OTel provider instance

    Raises:
        OpenTelemetryProviderException: If provider is not supported
    """

    if not provider_name:
        raise OpenTelemetryProviderException(provider_name, "Unsupported provider")
    elif provider_name == OTelProviderType.LANGSMITH.value:
        return LangsmithProvider(**kwargs)
    elif provider_name == OTelProviderType.AGENTA.value:
        return AgentaProvider(**kwargs)
    elif provider_name == OTelProviderType.LANGFUSE.value:
        return LangfuseProvider(**kwargs)
    elif provider_name == OTelProviderType.TRACELOOP.value:
        return TraceloopProvider(**kwargs)
    elif provider_name == OTelProviderType.BRAINTRUST.value:
        return BrainTrustProvider(**kwargs)
    elif provider_name == OTelProviderType.LAMINAR.value:
        return LaminarProvider(**kwargs)
    elif provider_name == OTelProviderType.OTELCOLLECTOR.value:
        return OTelCollectorProvider(**kwargs)
    else:
        raise OpenTelemetryProviderException(provider_name, "Unsupported provider")


def get_available_providers() -> list[str]:
    """Get list of available OpenTelemetry providers."""
    return [provider.value for provider in OTelProviderType]


# def create_provider_from_config(config: Dict[str, Any]) -> OTelProvider:
#     """Create a provider from configuration dictionary.

#     Args:
#         config: Configuration dictionary with 'type' key and provider-specific options

#     Returns:
#         Configured OTel provider instance

#     Example:
#         config = {
#             "type": "langsmith",
#             "project_name": "my-project",
#             "api_key": "sk-..."
#         }
#     """
#     provider_type = config.pop("type")
#     return create_otel_provider(provider_type, **config)
