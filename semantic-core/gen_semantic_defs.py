import json
import logging
import os
import textwrap
from typing import Optional

from pydantic import BaseModel, Field
from typing_extensions import Annotated

# Semantic Types

Hostname = Annotated[
    str,
    Field(
        description="""
        A hostname is a label that is assigned to a device connected to a computer network and that is used to identify the device in various forms of electronic communication, such as the World Wide Web.""",
        examples=["my-hostname"],
        min_length=1,
        json_schema_extra={"is_sensitive": False},
    ),
]

HttpStatusCode = Annotated[
    str,
    Field(
        description="""
        The HTTP response status code.""",
        examples=["200", "404", "500"],
        pattern=r"^[12345]\d\d$",
        json_schema_extra={"is_sensitive": False},
    ),
]

HttpUrl = Annotated[
    str,
    Field(
        description="""
        The URL on an HTTP request, including the obfuscated query string.""",
        examples=["https://example.com:443/search?q=datadog"],
        min_length=1,
        json_schema_extra={"is_sensitive": True},
    ),
]

HttpMethod = Annotated[
    str,
    Field(
        description="""
        The HTTP method used for the connection. Required for both client and server spans.""",
        examples=["GET", "POST", "PUT", "DELETE", "PATCH"],
        pattern=r"^(GET|HEAD|POST|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)$",
        json_schema_extra={"is_sensitive": False},
    ),
]

HttpVersion = Annotated[
    str,
    Field(
        description="""
        The version of HTTP used for the request.""",
        examples=["1.0", "1.1", "2.0"],
        pattern=r"^1\.[01]$|^2\.0$",
        json_schema_extra={"is_sensitive": False},
    ),
]

HttpRoute = Annotated[
    str,
    Field(
        description="""
        The matched route (path template) of an HTTP request.""",
        examples=["/users/:userID"],
        min_length=1,
        json_schema_extra={"is_sensitive": False},
    ),
]

HttpUserAgent = Annotated[
    str,
    Field(
        description="""
        The user agent header received with the request.""",
        examples=["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"],
        min_length=1,
        json_schema_extra={"is_sensitive": True},
    ),
]

HttpContentLength = Annotated[
    int,
    Field(
        description="""
        The size of the request or response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the Content-Length header.
        For requests using transport encoding, this should be compressed size.""",
        examples=[1234],
        gt=0,
        json_schema_extra={"is_sensitive": True},
    ),
]

IpAddress = Annotated[
    str,
    Field(
        description=textwrap.dedent(
            """
            An IP address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication."""
        ),
        examples=["192.168.123.132"],
        pattern=r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
        json_schema_extra={"is_sensitive": True},
    ),
]

# Semantic Models


class IntakeHttpSpan(BaseModel):
    """
    Semantic model for the HTTP information present in a span during intake.
    """

    http_status_code: Annotated[
        HttpStatusCode,
        Field(
            title="HTTP Status Code",
            alias="http.status_code",
            description=textwrap.dedent(
                """
                The HTTP response status code.
                When span.kind: client the response status code received.
                When span.kind: server the response status code sent.
                Note: Although this is an integer, it must be sent as a string."""
            ),
        ),
    ]
    http_url: Annotated[
        HttpUrl,
        Field(
            alias="http.url",
            title="HTTP URL",
            description=textwrap.dedent(
                """
            The URL of the HTTP request, including the obfuscated query string."""
            ),
        ),
    ]
    http_method: Annotated[
        HttpMethod,
        Field(
            alias="http.method",
            title="HTTP Method",
            description=textwrap.dedent(
                """
            The HTTP method used for the connection. Required for both client and server spans."""
            ),
        ),
    ]
    http_version: Annotated[
        HttpVersion,
        Field(
            alias="http.version",
            title="HTTP Version",
            description=textwrap.dedent(
                """
            The version of HTTP used for the request."""
            ),
        ),
    ]
    http_route: Optional[
        Annotated[
            HttpRoute,
            Field(
                alias="http.route",
                title="HTTP Route",
                description=textwrap.dedent(
                    """
            The matched route (path template).
            Only when span.kind: server."""
                ),
            ),
        ]
    ]
    http_client_ip: Optional[
        Annotated[
            IpAddress,
            Field(
                alias="http.client_ip",
                title="HTTP Client IP",
                description=textwrap.dedent(
                    """
            The IP address of the original client behind all proxies, if known (discovered from headers such as X-Forwarded-For)."""
                ),
            ),
        ]
    ]
    http_useragent: Optional[
        Annotated[
            HttpUserAgent,
            Field(
                alias="http.useragent",
                title="HTTP User Agent",
                description=textwrap.dedent(
                    """
            The user agent header received with the request.
            Only when span.kind: server."""
                ),
            ),
        ]
    ]
    http_request_content_length: Optional[
        Annotated[
            HttpContentLength,
            Field(
                alias="http.request.content_length",
                title="HTTP Request Content Length",
                description=textwrap.dedent(
                    """
            The size of the request body.
            The size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the Content-Length header.
            For requests using transport encoding, this should be compressed size."""
                ),
            ),
        ]
    ]
    http_response_content_length: Optional[
        Annotated[
            HttpContentLength,
            Field(
                alias="http.response.content_length",
                title="HTTP Response Content Length",
                description=textwrap.dedent(
                    """
            The size of the response payload body in bytes.
            The size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the Content-Length header.
            For requests using transport encoding, this should be compressed size."""
                ),
            ),
        ]
    ]
    http_request_content_length_uncompressed: Optional[
        Annotated[
            HttpContentLength,
            Field(
                alias="http.request.content_length_uncompressed",
                title="HTTP Request Content Length Uncompressed",
                description=textwrap.dedent(
                    """
            The size of the request payload body after transport decoding. Not set if transport encoding not used."""
                ),
            ),
        ]
    ]
    http_response_content_length_uncompressed: Optional[
        Annotated[
            HttpContentLength,
            Field(
                alias="http.response.content_length_uncompressed",
                title="HTTP Response Content Length Uncompressed",
                description=textwrap.dedent(
                    """
            The size of the response payload body after transport decoding. Not set if transport encoding not used."""
                ),
            ),
        ]
    ]


class IntakeSpan(BaseModel):
    hostname: Optional[
        Annotated[
            Hostname,
            Field(
                alias="_dd.hostname",
                title="Hostname",
                description=textwrap.dedent(
                    """
                When the DD_TRACE_REPORT_HOSTNAME=true environment variable, or report_hostname are set by the user the tracing clients will collect the hostname directly from the process or OS to report to the trace agent.
                When _dd.hostname is present the trace agent will not use it’s hostname for the trace.
                Note: this tag should only be set if configured to do so. It is disabled by default."""
                ),
            ),
        ]
    ]


class Schema(BaseModel):
    intake_span: IntakeSpan
    intake_http_span: IntakeHttpSpan


def generate_schema(version):
    json_schema_str = json.dumps(Schema.model_json_schema(), indent=2)

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
