# AI LLM Lab

A comprehensive Python application for experimenting with Large Language Models (LLMs) and observability through OpenTelemetry.
This project provides a modular architecture supporting multiple LLM providers and telemetry backends for monitoring,
tracing, and analyzing LLM interactions.

## Features

- **Multi-LLM Support**: Switch between different LLM providers seamlessly (Anthropic, OpenAI)
- **Comprehensive Observability**: Built-in OpenTelemetry integration with 6 telemetry providers
- **Modular Architecture**: Clean separation of concerns with dedicated packages for models, telemetry, and core logic
- **Environment-based Configuration**: Easy configuration through environment variables
- **Production-ready**: Comprehensive error handling and resource detection
- **Extensible Design**: Easy to add new LLM and telemetry providers

## Supported Providers

### LLM Providers

| Provider         | Models                                    | Configuration       |
| ---------------- | ----------------------------------------- | ------------------- |
| ✅ **Anthropic** | Claude 3 Opus, Sonnet, Haiku              | `ANTHROPIC_API_KEY` |
| **OpenAI**       | GPT-4, GPT-4 Turbo, GPT-3.5 Turbo, GPT-4o | `OPENAI_API_KEY`    |

### OpenTelemetry Providers

| Provider             | Description                          | Configuration                                |
| -------------------- | ------------------------------------ | -------------------------------------------- |
| ✅ **Langsmith**     | LangChain's observability platform   | `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT`     |
| ✅ **Langfuse**      | Open-source LLM engineering platform | `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY` |
| ✅ **AgentaAI**      | LLM evaluation and monitoring        | `AGENTA_API_KEY`, `AGENTA_APP_ID`            |
| ✅ **Traceloop**     | LLM observability and monitoring     | `TRACELOOP_API_KEY`                          |
| ✅ **BrainTrust**    | AI evaluation and observability      | `BRAINTRUST_API_KEY`                         |
| ✅ **Laminar**       | LLM observability and monitoring     | `LAMINAR_API_KEY`                            |
| ✅ **OTelCollector** | OpenTelemetry Collector instance     | `OTEL_EXPORTER_OTLP_ENDPOINT`                |

## Configuration

### Basic Configuration

Set the core environment variables to configure providers:

```shell
# Choose LLM Provider (anthropic or openai)
export LLM_PROVIDER=anthropic

# Choose OpenTelemetry Provider (langsmith, langfuse, agenta, traceloop, braintrust, laminar, or otelcollector)
export OTEL_PROVIDER=langfuse

# Choose Protocol (http or grpc)
export OTEL_EXPORTER_OTLP_PROTOCOL=http
```

### LLM Provider Configuration

#### Anthropic (Claude)

```shell
export ANTHROPIC_API_KEY=your_anthropic_api_key
export LLM_PROVIDER=anthropic
```

#### OpenAI (GPT)

```shell
export OPENAI_API_KEY=your_openai_api_key
export LLM_PROVIDER=openai
```

### OpenTelemetry Provider Configuration

#### Langsmith

```shell
export LANGSMITH_API_KEY=your_langsmith_api_key
export LANGSMITH_PROJECT=your_project_name
export OTEL_PROVIDER=langsmith
```

#### Langfuse

```shell
export LANGFUSE_PUBLIC_KEY=your_public_key
export LANGFUSE_SECRET_KEY=your_secret_key
export OTEL_PROVIDER=langfuse
```

#### AgentaAI

```shell
export AGENTA_API_KEY=your_agenta_api_key
export AGENTA_APP_ID=your_app_id
export OTEL_PROVIDER=agenta
```

#### Traceloop

```shell
export TRACELOOP_API_KEY=your_traceloop_api_key
export TRACELOOP_ENVIRONMENT=production  # Optional, defaults to "production"
export OTEL_PROVIDER=traceloop
```

#### BrainTrust

```shell
export BRAINTRUST_API_KEY=your_braintrust_api_key
export BRAINTRUST_PROJECT_NAME=ai-llm-lab       # Optional, defaults to "ai-llm-lab"
export OTEL_PROVIDER=braintrust
```

#### Laminar

```shell
export LAMINAR_API_KEY=your_laminar_api_key
export LAMINAR_TEAM_ID=your_team_id             # Optional
export OTEL_PROVIDER=laminar
```

#### OpenTelemetry Collector

```shell
# For local collector (default)
export OTEL_PROVIDER=otelcollector
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317  # gRPC (default)
# OR
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318  # HTTP
export OTEL_EXPORTER_OTLP_PROTOCOL=http
```

## Installation

### Prerequisites

- Python 3.13+
- uv (Python package manager)

### Install Dependencies

```shell
uv install
```

## Usage

### Basic Usage

```shell
uv run src/app.py
```

### Example Configurations

#### Example 1: Anthropic + Langfuse

```shell
# Configure for Anthropic + Langfuse
export LLM_PROVIDER=anthropic
export ANTHROPIC_API_KEY=your_anthropic_key
export OTEL_PROVIDER=langfuse
export LANGFUSE_PUBLIC_KEY=your_public_key
export LANGFUSE_SECRET_KEY=your_secret_key
export OTEL_EXPORTER_OTLP_PROTOCOL=http

# Run the application
uv run src/app.py
```

#### Example 2: OpenAI + Langsmith

```shell
# Configure for OpenAI + Langsmith
export LLM_PROVIDER=openai
export OPENAI_API_KEY=your_openai_key
export OTEL_PROVIDER=langsmith
export LANGSMITH_API_KEY=your_langsmith_key
export LANGSMITH_PROJECT=my-ai-project
export OTEL_EXPORTER_OTLP_PROTOCOL=http

# Run the application
uv run src/app.py
```

#### Example 3: Anthropic + BrainTrust

```shell
# Configure for Anthropic + BrainTrust
export LLM_PROVIDER=anthropic
export ANTHROPIC_API_KEY=your_anthropic_key
export OTEL_PROVIDER=braintrust
export BRAINTRUST_API_KEY=your_braintrust_key
export BRAINTRUST_PROJECT_NAME=ai-experiment
export OTEL_EXPORTER_OTLP_PROTOCOL=http

# Run the application
uv run src/app.py
```

#### Example 4: OpenAI + Local OpenTelemetry Collector

```shell
# Configure for OpenAI + Local OTel Collector
export LLM_PROVIDER=openai
export OPENAI_API_KEY=your_openai_key
export OTEL_PROVIDER=otelcollector
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc

# Run the application
uv run src/app.py
```

## Architecture

The project follows a clean, modular architecture:

### Factory Pattern

- **LLM Factory** (`models/factory.py`): Creates LLM instances based on provider name
- **Telemetry Factory** (`telemetry/providers/factory.py`): Creates telemetry provider instances

### Provider Interface

- All telemetry providers implement the `OTelProvider` base class
- Consistent interface for endpoints, headers, and authentication
- Easy to extend with new providers

### Resource Detection

- Automatic detection of environment resources (process, OS, host)
- Comprehensive service metadata for better observability
- Configurable resource attributes
