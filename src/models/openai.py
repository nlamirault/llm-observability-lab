# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""OpenAI GPT model implementation."""

from langchain_openai import ChatOpenAI


def create_openai_llm(model: str = "gpt-4", api_key: str = None) -> ChatOpenAI:
    """Create and configure OpenAI GPT LLM instance."""
    kwargs = {"model": model}
    if api_key:
        kwargs["api_key"] = api_key
    return ChatOpenAI(**kwargs)


def get_default_model() -> str:
    """Get the default OpenAI model."""
    return "gpt-4"


def get_available_models() -> list[str]:
    """Get list of available OpenAI models."""
    return [
        "gpt-4",
        "gpt-4-turbo",
        "gpt-3.5-turbo",
        "gpt-4o",
        "gpt-4o-mini",
    ]
