# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Base interface for OpenTelemetry providers."""

from abc import ABC, abstractmethod
from typing import Dict, Optional


class OTelProvider(ABC):
    """Base class for OpenTelemetry providers."""

    @abstractmethod
    def get_endpoint(self) -> str:
        """Get the OpenTelemetry endpoint for the provider.

        Args:
            protocol: The protocol to use (http or grpc)

        Returns:
            The endpoint URL
        """
        pass

    @abstractmethod
    def get_headers(self) -> Dict[str, str]:
        """Get the required headers for authentication.

        Returns:
            Dictionary of headers
        """
        pass

    @abstractmethod
    def get_project_name(self) -> Optional[str]:
        """Get the project name if applicable.

        Returns:
            Project name or None
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Get the provider name."""
        pass
