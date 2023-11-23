import json
import logging
import os
import textwrap
from enum import Enum

from pydantic import BaseModel, Field


class Availability(Enum):
    MANDATORY = (0, "Datadog will ensure that this value is sent.")
    BEST_EFFORT = (
        1,
        "Datadog will try to send this value, but will not fail if it is not possible.",
    )
    OPT_IN = (
        2,
        "The availability of this value depends on the configuration of the client.",
    )


class Fields(BaseModel):
    hostname: str = Field(
        alias="_dd.hostname",
        title="Hostname",
        description=textwrap.dedent(
            """
            When the DD_TRACE_REPORT_HOSTNAME=true environment variable, or report_hostname are set by the user the tracing clients will collect the hostname directly from the process or OS to report to the trace agent.
            When _dd.hostname is present the trace agent will not use it’s hostname for the trace.
            Note: this tag should only be set if configured to do so. It is disabled by default."""
        ),
        examples=["my-hostname"],
        min_length=1,
        json_schema_extra={
            "availability": Availability.BEST_EFFORT,
            "is_sensitive": False,
        },
    )
    http_status_code: str = Field(
        alias="http.status_code",
        title="HTTP Status Code",
        description=textwrap.dedent(
            """
            The HTTP response status code.
            When span.kind: client the response status code received.
            When span.kind: server the response status code sent.
            Note: Although this is an integer, it must be sent as a string."""
        ),
        examples=["200", "404", "500"],
        pattern=r"^[12345]\d\d$",
        json_schema_extra={
            "availability": Availability.MANDATORY,
            "is_sensitive": False,
        },
    )
    http_url: str = Field(
        alias="http.url",
        title="HTTP URL",
        description=textwrap.dedent(
            """
            The URL of the HTTP request, including the obfuscated query string."""
        ),
        examples=["https://example.com:443/search?q=datadog"],
        min_length=1,
        json_schema_extra={
            "availability": Availability.MANDATORY,
            "is_sensitive": True,
        },
    )
    http_method: str = Field(
        alias="http.method",
        title="HTTP Method",
        description=textwrap.dedent(
            """
            The HTTP method used for the connection. Required for both client and server spans."""
        ),
        examples=["GET", "POST", "PUT", "DELETE", "PATCH"],
        pattern=r"^(GET|HEAD|POST|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)$",
        json_schema_extra={
            "availability": Availability.MANDATORY,
            "is_sensitive": False,
        },
    )
    http_version: str = Field(
        alias="http.version",
        title="HTTP Version",
        description=textwrap.dedent(
            """
            The version of HTTP used for the request."""
        ),
        examples=["1.0", "1.1", "2.0"],
        pattern=r"^1\.[01]$|^2\.0$",
        json_schema_extra={
            "availability": Availability.BEST_EFFORT,
            "is_sensitive": False,
        },
    )
    http_route: str = Field(
        alias="http.route",
        title="HTTP Route",
        description=textwrap.dedent(
            """
            The matched route (path template).
            Only when span.kind: server."""
        ),
        examples=["/users/:userID"],
        min_length=1,
        json_schema_extra={
            "availability": Availability.BEST_EFFORT,
            "is_sensitive": False,
        },
    )
    http_client_ip: str = Field(
        alias="http.client_ip",
        title="HTTP Client IP",
        description=textwrap.dedent(
            """
            The IP address of the original client behind all proxies, if known (discovered from headers such as X-Forwarded-For)."""
        ),
        examples=["192.168.123.132"],
        pattern=r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
        json_schema_extra={
            "availability": Availability.BEST_EFFORT,
            "is_sensitive": True,
        },
    )
    http_useragent: str = Field(
        alias="http.useragent",
        title="HTTP User Agent",
        description=textwrap.dedent(
            """
            The user agent header received with the request.
            Only when span.kind: server."""
        ),
        examples=["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"],
        min_length=1,
        json_schema_extra={
            "availability": Availability.BEST_EFFORT,
            "is_sensitive": True,
        },
    )
    http_request_content_length: int = Field(
        alias="http.request.content_length",
        title="HTTP Request Content Length",
        description=textwrap.dedent(
            """
            The size of the request body.
            The size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the Content-Length header.
            For requests using transport encoding, this should be compressed size."""
        ),
        examples=[1234],
        gt=0,
        json_schema_extra={
            "availability": Availability.BEST_EFFORT,
            "is_sensitive": True,
        },
    )
    http_response_content_length: int = Field(
        alias="http.response.content_length",
        title="HTTP Response Content Length",
        description=textwrap.dedent(
            """
            The size of the response payload body in bytes.
            The size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the Content-Length header.
            For requests using transport encoding, this should be compressed size."""
        ),
        examples=[1234],
        gt=0,
        json_schema_extra={
            "availability": Availability.BEST_EFFORT,
            "is_sensitive": True,
        },
    )
    http_request_content_length_uncompressed: int = Field(
        alias="http.request.content_length_uncompressed",
        title="HTTP Request Content Length Uncompressed",
        description=textwrap.dedent(
            """
            The size of the request payload body after transport decoding. Not set if transport encoding not used."""
        ),
        examples=[1234],
        gt=0,
        json_schema_extra={
            "availability": Availability.BEST_EFFORT,
            "is_sensitive": True,
        },
    )
    http_response_content_length_uncompressed: int = Field(
        alias="http.response.content_length_uncompressed",
        title="HTTP Response Content Length Uncompressed",
        description=textwrap.dedent(
            """
            The size of the response payload body after transport decoding. Not set if transport encoding not used."""
        ),
        examples=[1234],
        gt=0,
        json_schema_extra={
            "availability": Availability.BEST_EFFORT,
            "is_sensitive": True,
        },
    )


def generate_schema(version):
    json_schema_str = json.dumps(Fields.model_json_schema(), indent=2)

    # Create the directory if it doesn't exist
    output_dir = os.path.join(os.getcwd(), version)
    os.makedirs(output_dir, exist_ok=True)

    # Write the schema to the specified file
    output_file = os.path.join(output_dir, "schema.json")
    with open(output_file, "w") as f:
        f.write(json_schema_str)


if __name__ == "__main__":
    import argparse

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Generate schema JSON file.")
    parser.add_argument("version", type=str, help="Specify the version")

    args = parser.parse_args()

    try:
        generate_schema(version=args.version)
        logger.info(f"Schema successfully generated for version: {args.version}")
    except Exception as e:
        logger.error(f"Error generating schema: {e}")
