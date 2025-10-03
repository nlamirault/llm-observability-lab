# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""BrainTrust OpenTelemetry provider."""

from os import environ
from typing import Dict, Optional

from .base import OTelProvider
from exceptions import OpenTelemetryProviderError


BRAINTRUST_CLOUD_ENDPOINT = "https://api.braintrust.dev/otel"


class BrainTrustProvider(OTelProvider):
    """BrainTrust OpenTelemetry provider implementation."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        project_name: Optional[str] = None,
    ):
        """Initialize BrainTrust provider.

        Args:
            api_key: BrainTrust API key (defaults to env BRAINTRUST_API_KEY)
            project_name: BrainTrust project name (defaults to env BRAINTRUST_PROJECT_NAME)
        """

        self.api_key = api_key or environ.get("BRAINTRUST_API_KEY")
        self.project_name = project_name or environ.get("BRAINTRUST_PROJECT_NAME")

        if not self.api_key:
            raise OpenTelemetryProviderError(
                "braintrust",
                "BrainTrust API key is required. Set BRAINTRUST_API_KEY environment variable.",
            )

        print("BrainTrust OpenTelemetry provider setup done")

    def get_endpoint(self) -> str:
        """Get the BrainTrust OpenTelemetry endpoint."""
        return BRAINTRUST_CLOUD_ENDPOINT

    def get_headers(self) -> Dict[str, str]:
        """Get BrainTrust authentication headers."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "x-bt-parent": f"project_name:{self.project_name}",
        }
        return headers

    def get_project_name(self) -> Optional[str]:
        """Get the BrainTrust project name."""
        return self.project_name

    @property
    def name(self) -> str:
        """Get the provider name."""
        return "braintrust"
