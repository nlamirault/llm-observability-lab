# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

# import agenta as ag
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain, SequentialChain, TransformChain


def langchain_app(llm):
    # Define a transformation chain to create the prompt
    transform = TransformChain(
        input_variables=["subject"],
        output_variables=["prompt"],
        transform=lambda inputs: {
            "prompt": f"Tell me a joke about {inputs['subject']}."
        },
    )

    # Define the first LLM chain to generate a joke
    first_prompt_messages = [
        SystemMessage(content="You are a funny sarcastic nerd."),
        HumanMessage(content="{prompt}"),
    ]
    first_prompt_template = ChatPromptTemplate.from_messages(first_prompt_messages)
    first_chain = LLMChain(llm=llm, prompt=first_prompt_template, output_key="joke")

    # Define the second LLM chain to translate the joke
    second_prompt_messages = [
        SystemMessage(content="You are an Elf."),
        HumanMessagePromptTemplate.from_template(
            "Translate the joke below into Sindarin language:\n{joke}"
        ),
    ]
    second_prompt_template = ChatPromptTemplate.from_messages(second_prompt_messages)
    second_chain = LLMChain(llm=llm, prompt=second_prompt_template)

    # Chain everything together in a sequential workflow
    workflow = SequentialChain(
        chains=[transform, first_chain, second_chain],
        input_variables=["subject"],
    )

    # Execute the workflow and print the result
    result = workflow({"subject": "OpenTelemetry"})
    print(result)
