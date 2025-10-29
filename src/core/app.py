# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""Main application logic."""

from models.factory import create_llm
from models.llm import create_test_messages
from telemetry.resource import create_resource
from telemetry.tracing import cleanup_tracing, setup_tracing_with_provider


def run_application(
    llm_provider: str = "anthropic",
    otel_provider: str = None,
    otel_protocol: str = None,
):
    """Run the main application.

    Args:
        llm_provider: LLM provider to use (anthropic or openai)
        model: Specific model name (optional, uses provider default)
        otel_provider: OpenTelemetry provider to use (langsmith or agenta)
        otel_protocol: Protocol to use for tracing (http or grpc)
    """
    print(f"OTEL: {otel_provider} {otel_protocol}")
    custom_resource = create_resource("ai-llm-lab")
    setup_tracing_with_provider(otel_provider, otel_protocol, custom_resource)

    # Initialize Paid client (commented out)
    # client = Paid(token="59878f8d-be5c-4401-b0ff-4551ae74858d")
    # client.initialize_tracing()

    # Set up LLM using factory
    llm = create_llm(provider=llm_provider, model=None)
    print(f"Using {llm_provider} LLM with {otel_provider} telemetry")

    messages = create_test_messages()
    result = llm.invoke(messages).content
    print("LLM output:\n", result)

    # chain.langchain_app(llm)

    # Trace LangChain calls to track costs (commented out)
    # def make_langchain_call():
    #     messages = [HumanMessage(content="What is the weather for today at Bordeaux/France")]
    #     response = llm.invoke(messages)
    #     return response

    # result = client.trace(
    #     external_customer_id="onboarding-test-customer",
    #     external_agent_id="ai-sdk-chatbot-id",
    #     fn=lambda: make_langchain_call(),
    # )

    cleanup_tracing()
