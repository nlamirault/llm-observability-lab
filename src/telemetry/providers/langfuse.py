# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Langfuse OpenTelemetry provider."""

import base64
from os import environ
from typing import Dict, Optional

from .base import OTelProvider
from exceptions import OpenTelemetryProviderException


LANGFUSE_CLOUD_ENDPOINT = "https://cloud.langfuse.com/api/public/otel"


class LangfuseProvider(OTelProvider):
    """Langfuse OpenTelemetry provider implementation."""

    def __init__(
        self,
        secret_key: Optional[str] = None,
        public_key: Optional[str] = None,
    ):
        """Initialize Langfuse provider.

        Args:
            api_key: Langfuse API key (defaults to env LANGFUSE_API_KEY)
            secret_key: Langfuse secret key (defaults to env LANGFUSE_SECRET_KEY)
        """
        self.secret_key = secret_key or environ.get("LANGFUSE_SECRET_KEY")
        self.public_key = public_key or environ.get("LANGFUSE_PUBLIC_KEY")

        if not self.public_key:
            raise OpenTelemetryProviderException(
                "langfuse",
                "Langfuse API key is required. Set LANGFUSE_PUBLIC_KEY environment variable.",
            )
        if not self.secret_key:
            raise OpenTelemetryProviderException(
                "langfuse",
                "Langfuse secret key is required. Set LANGFUSE_SECRET_KEY environment variable.",
            )

        print("Langfuse OpenTelemetry provider setup done")

    def get_endpoint(self) -> str:
        """Get the Langfuse OpenTelemetry endpoint."""
        return LANGFUSE_CLOUD_ENDPOINT

    def get_headers(self) -> Dict[str, str]:
        """Get Langfuse authentication headers."""
        auth = base64.b64encode(
            f"{self.public_key}:{self.secret_key}".encode()
        ).decode()
        headers = {
            "Authorization": f"Basic {auth}",
        }
        return headers

    def get_project_name(self) -> Optional[str]:
        """Get the project name (not directly applicable for Langfuse)."""
        return self.public_key if self.public_key else None

    @property
    def name(self) -> str:
        """Get the provider name."""
        return "langfuse"
