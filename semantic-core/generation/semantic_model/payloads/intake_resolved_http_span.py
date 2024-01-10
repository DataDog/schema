import textwrap
from typing import Annotated
from pydantic import Field, BaseModel

from semantic_model.registry.types import HttpStatusCode
from semantic_model.registry.types import HttpUrl
from semantic_model.registry.types import HttpMethod
from semantic_model.registry.types import HttpVersion
from semantic_model.registry.types import HttpRoute
from semantic_model.registry.types import IpAddress
from semantic_model.registry.types import HttpUserAgent
from semantic_model.registry.types import HttpContentLength


class IntakeResolvedHttpSpan(BaseModel):
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
    ] = ...
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
    ] = ...
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
    ] = ...
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
    ] = ...
    http_route: Annotated[
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
    ] = None
    http_client_ip: Annotated[
        IpAddress,
        Field(
            alias="http.client_ip",
            title="HTTP Client IP",
            description=textwrap.dedent(
                """
            The IP address of the original client behind all proxies, if known (discovered from headers such as X-Forwarded-For)."""
            ),
        ),
    ] = None
    http_useragent: Annotated[
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
    ] = None
    http_request_content_length: Annotated[
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
    ] = None
    http_response_content_length: Annotated[
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
    ] = None
    http_request_content_length_uncompressed: Annotated[
        HttpContentLength,
        Field(
            alias="http.request.content_length_uncompressed",
            title="HTTP Request Content Length Uncompressed",
            description=textwrap.dedent(
                """
            The size of the request payload body after transport decoding. Not set if transport encoding not used."""
            ),
        ),
    ] = None
    http_response_content_length_uncompressed: Annotated[
        HttpContentLength,
        Field(
            alias="http.response.content_length_uncompressed",
            title="HTTP Response Content Length Uncompressed",
            description=textwrap.dedent(
                """
            The size of the response payload body after transport decoding. Not set if transport encoding not used."""
            ),
        ),
    ] = None
