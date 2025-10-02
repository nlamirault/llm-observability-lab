# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

from os import environ

from core.app import run_application


def main():
    run_application(
        environ.get("LLM_PROVIDER"),
        environ.get("OTEL_PROVIDER"),
        environ.get("OTEL_EXPORTER_OTLP_PROTOCOL"),
    )


if __name__ == "__main__":
    main()
