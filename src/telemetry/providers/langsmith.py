# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Langsmith OpenTelemetry provider."""

from os import environ
from typing import Dict, Optional

from .base import OTelProvider
from exceptions import OpenTelemetryProviderException


LANGSMITH_ENDPOINT = "https://api.smith.langchain.com/otel"


class LangsmithProvider(OTelProvider):
    """Langsmith OpenTelemetry provider implementation."""

    def __init__(
        self, project_name: Optional[str] = None, api_key: Optional[str] = None
    ):
        """Initialize Langsmith provider.

        Args:
            project_name: Langsmith project name (defaults to env LANGSMITH_PROJECT)
            api_key: Langsmith API key (defaults to env LANGSMITH_API_KEY)
        """
        self.project_name = project_name or environ.get("LANGSMITH_PROJECT")
        self.api_key = api_key or environ.get("LANGSMITH_API_KEY")

        if not self.api_key:
            raise OpenTelemetryProviderException(
                "langsmith",
                "Langsmith API key is required. Set LANGSMITH_API_KEY environment variable.",
            )
        print("Langsmith OpenTelemetry provider setup done")

    def get_endpoint(self) -> str:
        """Get the Langsmith OpenTelemetry endpoint."""
        return LANGSMITH_ENDPOINT

    def get_headers(self) -> Dict[str, str]:
        """Get Langsmith authentication headers."""
        return {
            "x-api-key": self.api_key,
            "Langsmith-Project": self.project_name,
        }

    def get_project_name(self) -> Optional[str]:
        """Get the Langsmith project name."""
        return self.project_name

    @property
    def name(self) -> str:
        """Get the provider name."""
        return "langsmith"
