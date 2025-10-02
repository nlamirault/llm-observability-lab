# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0


class AILLMLab(Exception):
    """Base exception for application."""

    status_code = 500


class OpenTelemetryProtocolException(AILLMLab):
    def __init__(self, protocol, message="Unsupported protocol"):
        self.protocol = protocol
        self.message = message
        super().__init__(f"{message}: {protocol}")


class OpenTelemetryProviderException(AILLMLab):
    def __init__(self, provider, message):
        self.provider = provider
        self.message = message
        super().__init__(f"{provider}: {message}")
