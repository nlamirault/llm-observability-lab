# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""AgentaAI OpenTelemetry provider."""

from os import environ
from typing import Dict, Optional

from .base import OTelProvider
from exceptions import OpenTelemetryProviderError


AGENTA_AI_ENDPOINT = "https://cloud.agenta.ai/api/otlp"


class AgentaProvider(OTelProvider):
    """AgentaAI OpenTelemetry provider implementation."""

    def __init__(
        self,
        api_key: Optional[str] = None,
    ):
        """Initialize Agenta provider.

        Args:
            api_key: Agenta API key (defaults to env AGENTA_API_KEY)
        """
        self.api_key = api_key or environ.get("AGENTA_API_KEY")

        if not self.api_key:
            raise OpenTelemetryProviderError(
                "agenta",
                "Agenta API key is required. Set AGENTA_API_KEY environment variable.",
            )
        print("Agenta OpenTelemetry provider setup done")

    def get_endpoint(self) -> str:
        """Get the Agenta OpenTelemetry endpoint."""
        return AGENTA_AI_ENDPOINT

    def get_headers(self) -> Dict[str, str]:
        """Get Agenta authentication headers."""
        headers = {
            "Authorization": f"ApiKey {self.api_key}",
        }
        return headers

    def get_project_name(self) -> Optional[str]:
        """Get the Agenta application ID as project name."""
        return None  # Agenta doesn't use app_id in this implementation

    @property
    def name(self) -> str:
        """Get the provider name."""
        return "agenta"
