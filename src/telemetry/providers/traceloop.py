# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Traceloop OpenTelemetry provider."""

from os import environ
from typing import Dict, Optional

from .base import OTelProvider
from exceptions import OpenTelemetryProviderError


TRACELOOP_CLOUD_ENDPOINT = "https://api.traceloop.com"


class TraceloopProvider(OTelProvider):
    """Traceloop OpenTelemetry provider implementation."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        destination_id: Optional[str] = None,
    ):
        """Initialize Traceloop provider.

        Args:
            api_key: Traceloop API key (defaults to env TRACELOOP_API_KEY)
            destination_id: Traceloop destination (defaults to env TRACELOOP_DESTINATION or "production")
        """
        self.api_key = api_key or environ.get("TRACELOOP_API_KEY")
        self.environment = destination_id or environ.get(
            "TRACELOOP_DESTINATION", "production"
        )

        if not self.api_key:
            raise OpenTelemetryProviderError(
                "traceloop",
                "Traceloop API key is required. Set TRACELOOP_API_KEY environment variable.",
            )

        print("Traceloop OpenTelemetry provider setup done")

    def get_endpoint(self) -> str:
        """Get the Traceloop OpenTelemetry endpoint."""
        return TRACELOOP_CLOUD_ENDPOINT

    def get_headers(self) -> Dict[str, str]:
        """Get Traceloop authentication headers."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            # "x-traceloop-destination-id": self.destination_id,
        }

    def get_project_name(self) -> Optional[str]:
        """Get the Traceloop environment as project name."""
        return self.environment

    @property
    def name(self) -> str:
        """Get the provider name."""
        return "traceloop"
