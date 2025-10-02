# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Anthropic Claude model implementation."""

from langchain_anthropic import ChatAnthropic


def create_anthropic_llm(model: str = "claude-3-opus-20240229") -> ChatAnthropic:
    """Create and configure Anthropic Claude LLM instance."""
    return ChatAnthropic(model=model)


def get_default_model() -> str:
    """Get the default Anthropic model."""
    return "claude-3-opus-20240229"


def get_available_models() -> list[str]:
    """Get list of available Anthropic models."""
    return [
        "claude-3-opus-20240229",
        "claude-3-sonnet-20240229",
        "claude-3-haiku-20240307",
    ]
