# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Laminar OpenTelemetry provider."""

from os import environ
from typing import Dict, Optional

from .base import OTelProvider
from exceptions import OpenTelemetryProviderError


LAMINAR_CLOUD_ENDPOINT = "https://api.lmnr.ai:8443"


class LaminarProvider(OTelProvider):
    """Laminar OpenTelemetry provider implementation."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        team_id: Optional[str] = None,
        base_url: Optional[str] = None,
        environment: Optional[str] = None,
    ):
        """Initialize Laminar provider.

        Args:
            api_key: Laminar API key (defaults to env LAMINAR_API_KEY)
            team_id: Laminar team ID (defaults to env LAMINAR_TEAM_ID)
        """
        self.api_key = api_key or environ.get("LAMINAR_API_KEY")
        self.project_id = team_id or environ.get("LAMINAR_TEAM_ID")

        if not self.api_key:
            raise OpenTelemetryProviderError(
                "laminar",
                "Laminar API key is required. Set LAMINAR_API_KEY environment variable.",
            )

        print("Laminar OpenTelemetry provider setup done")

    def get_endpoint(self) -> str:
        """Get the Laminar OpenTelemetry endpoint."""
        return LAMINAR_CLOUD_ENDPOINT

    def get_headers(self) -> Dict[str, str]:
        """Get Laminar authentication headers."""
        headers = {
            "authorization": f"Bearer {self.api_key}",
            # "x-laminar-team": self.team_id,
        }
        return headers

    def get_project_name(self) -> Optional[str]:
        """Get the Laminar project ID as project name."""
        return self.project_id

    @property
    def name(self) -> str:
        """Get the provider name."""
        return "laminar"
