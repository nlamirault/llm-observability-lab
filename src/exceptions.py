# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0


class LLMObservabilityLabError(Exception):
    """Base exception for all llm-LLMObservabilityLab errors.

    This is the base class for all LLMObservabilityLab-specific exceptions.

    Attributes:
        message (str): Human-readable error message.
        error_code (str): Unique error identifier for programmatic handling.
        details (dict): Additional context about the error.
        suggestion (str): User-friendly suggestion for resolving the error.
        debug_info (dict): Technical debugging information.

    Example:
        raise LLMObservabilityLab(
            message="Internal operation failed",
            error_code="500",
        )
    """

    error_code = 500

    def __init__(
        self,
        message: str,
        error_code: str = 500,
    ):
        """Initialize a LLMObservabilityLabError.

        Args:
            message: Human-readable error message.
            error_code: Rrror identifier.
        """
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)


class OpenTelemetryProtocolError(LLMObservabilityLabError):
    def __init__(self, protocol, message="Unsupported protocol"):
        self.protocol = protocol
        self.message = message
        super().__init__(f"{message}: {protocol}")


class OpenTelemetryProviderError(LLMObservabilityLabError):
    def __init__(self, provider, message):
        self.provider = provider
        self.message = message
        super().__init__(f"{provider}: {message}")
