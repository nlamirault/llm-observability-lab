# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Common LLM utilities and test messages."""

from langchain_core.messages import HumanMessage, SystemMessage


def create_test_messages():
    """Create sample test messages."""
    return [
        SystemMessage(content="You are a helpful assistant!"),
        HumanMessage(content="What is the capital of France?"),
    ]
