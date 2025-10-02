# SPDX-FileCopyrightText: Copyright (C) Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

"""OpenTelemetry resource configuration with multiple detectors."""

from opentelemetry.sdk import resources
# from opentelemetry.sdk.resources import (
#     ProcessResourceDetector,
#     OSResourceDetector,
#     HostResourceDetector,
#     ContainerResourceDetector,
# )

import version


def create_resource(service_name: str) -> resources.Resource:
    """Create OpenTelemetry resource with comprehensive detection.

    Args:
        service_name: Name of the service for telemetry

    Returns:
        Configured OpenTelemetry resource with detected attributes
    """
    # Create custom resource with service information
    custom = resources.Resource.create(
        {
            resources.SERVICE_NAME: service_name,
            resources.SERVICE_VERSION: version.__version__,
            "service.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.language": "python",
        }
    )

    # Detect environment resources
    detected = resources.get_aggregated_resources(
        [
            resources.ProcessResourceDetector(),  # Process info (PID, executable, etc.)
            resources.OsResourceDetector(),  # OS info (type, version, etc.)
            resources.OTELResourceDetector(),
        ]
    )

    return detected.merge(custom)


# def get_tracer() -> trace.Tracer:
#     """Returns the OpenTelemetry tracer instance."""
#     return trace.get_tracer(settings.OTEL_SERVICE_NAME)


# def get_meter() -> metrics.Meter:
#     """Returns the OpenTelemetry meter instance."""
#     return metrics.get_meter(settings.OTEL_SERVICE_NAME)
