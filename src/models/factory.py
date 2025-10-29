# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""LLM factory for creating different model instances."""

from enum import Enum
from typing import Union

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

from .anthropic import (
    create_anthropic_llm,
)
from .anthropic import (
    get_available_models as get_anthropic_models,
)
from .openai import create_openai_llm
from .openai import get_available_models as get_openai_models


class LLMProvider(Enum):
    """Supported LLM providers."""

    ANTHROPIC = "anthropic"
    OPENAI = "openai"


def create_llm(provider: Union[LLMProvider, str], model: str = None, **kwargs) -> Union[ChatAnthropic, ChatOpenAI]:
    """Create an LLM instance based on the provider.

    Args:
        provider: The LLM provider (anthropic or openai)
        model: The specific model name (optional, uses default if not provided)
        **kwargs: Additional arguments passed to the model constructor

    Returns:
        Configured LLM instance

    Raises:
        ValueError: If provider is not supported
    """
    if isinstance(provider, str):
        try:
            provider = LLMProvider(provider.lower())
        except ValueError:
            raise ValueError(f"Unsupported provider: {provider}")

    if provider == LLMProvider.ANTHROPIC:
        if model is None:
            from .anthropic import get_default_model

            model = get_default_model()
        return create_anthropic_llm(model=model, **kwargs)

    elif provider == LLMProvider.OPENAI:
        if model is None:
            from .openai import get_default_model

            model = get_default_model()
        return create_openai_llm(model=model, **kwargs)

    else:
        raise ValueError(f"Unsupported provider: {provider}")


def get_available_providers() -> list[str]:
    """Get list of available LLM providers."""
    return [provider.value for provider in LLMProvider]


def get_available_models(provider: Union[LLMProvider, str]) -> list[str]:
    """Get list of available models for a provider."""
    if isinstance(provider, str):
        provider = LLMProvider(provider.lower())

    if provider == LLMProvider.ANTHROPIC:
        return get_anthropic_models()
    elif provider == LLMProvider.OPENAI:
        return get_openai_models()
    else:
        raise ValueError(f"Unsupported provider: {provider}")
