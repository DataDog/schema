#!/usr/bin/env python

import json
import logging
import os
import re
import textwrap
from typing import List, Dict
from typing import NamedTuple

from pydantic import BaseModel, Field
from typing_extensions import Annotated

import type_registry as types

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Semantic Models


class IntakeResolvedHttpSpan(BaseModel):
    """
    Semantic model for the HTTP information present in a span during intake.
    """

    http_status_code: Annotated[
        types.HttpStatusCode,
        Field(
            title="HTTP Status Code",
            alias="meta.http.status_code",
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
        types.HttpUrl,
        Field(
            alias="meta.http.url",
            title="HTTP URL",
            description=textwrap.dedent(
                """
            The URL of the HTTP request, including the obfuscated query string."""
            ),
        ),
    ] = ...
    http_method: Annotated[
        types.HttpMethod,
        Field(
            alias="meta.http.method",
            title="HTTP Method",
            description=textwrap.dedent(
                """
            The HTTP method used for the connection. Required for both client and server spans."""
            ),
        ),
    ] = ...
    http_version: Annotated[
        types.HttpVersion,
        Field(
            alias="meta.http.version",
            title="HTTP Version",
            description=textwrap.dedent(
                """
            The version of HTTP used for the request."""
            ),
        ),
    ] = ...
    http_route: Annotated[
        types.HttpRoute,
        Field(
            alias="meta.http.route",
            title="HTTP Route",
            description=textwrap.dedent(
                """
            The matched route (path template).
            Only when span.kind: server."""
            ),
        ),
    ] = None
    http_client_ip: Annotated[
        types.IpAddress,
        Field(
            alias="meta.http.client_ip",
            title="HTTP Client IP",
            description=textwrap.dedent(
                """
            The IP address of the original client behind all proxies, if known (discovered from headers such as X-Forwarded-For)."""
            ),
        ),
    ] = None
    http_useragent: Annotated[
        types.HttpUserAgent,
        Field(
            alias="meta.http.useragent",
            title="HTTP User Agent",
            description=textwrap.dedent(
                """
            The user agent header received with the request.
            Only when span.kind: server."""
            ),
        ),
    ] = None
    http_request_content_length: Annotated[
        types.HttpContentLength,
        Field(
            alias="metrics.http.request.content_length_bytes",
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
        types.HttpContentLength,
        Field(
            alias="metrics.http.response.content_length_bytes",
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
        types.HttpContentLength,
        Field(
            alias="metrics.http.request.content_length_uncompressed",
            title="HTTP Request Content Length Uncompressed",
            description=textwrap.dedent(
                """
            The size of the request payload body after transport decoding. Not set if transport encoding not used."""
            ),
        ),
    ] = None
    http_response_content_length_uncompressed: Annotated[
        types.HttpContentLength,
        Field(
            alias="metrics.http.response.content_length_uncompressed",
            title="HTTP Response Content Length Uncompressed",
            description=textwrap.dedent(
                """
            The size of the response payload body after transport decoding. Not set if transport encoding not used."""
            ),
        ),
    ] = None


class IntakeResolvedDbSpan(BaseModel):
    """
    Semantic model for the DB information present in a span during intake.
    """

    db_system: Annotated[
        types.DbSystem,
        Field(
            alias="meta.db.system",
            title="DB System",
        ),
    ] = ...
    db_connection_string: Annotated[
        types.DbConnectionString,
        Field(
            alias="meta.db.connection_string",
            title="DB Connection String",
        ),
    ] = None
    db_user: Annotated[
        types.DbUser,
        Field(
            alias="meta.db.user",
            title="DB User",
        ),
    ] = None
    db_name: Annotated[
        types.DbName,
        Field(
            alias="db.name",
            title="DB Name",
        ),
    ] = None
    db_statement: Annotated[
        types.DbStatement,
        Field(
            alias="meta.db.statement",
            title="DB Statement",
        ),
    ] = None
    db_operation: Annotated[
        types.DbOperation,
        Field(
            alias="meta.db.operation",
            title="DB Operation",
        ),
    ] = None
    db_sql_table: Annotated[
        types.DbSqlTable,
        Field(
            alias="meta.db.sql.table",
            title="DB SQL Table",
        ),
    ] = None
    db_row_count: Annotated[
        types.DbRowCount,
        Field(
            alias="metrics.db.row_count",
            title="DB Row Count",
        ),
    ] = None


class SpanLink(BaseModel):
    traceID: Annotated[
        types.TraceId,
        Field(
            alias="traceID",
            title="Trace ID",
        ),
    ] = ...
    traceID_High: Annotated[
        types.TraceId,
        Field(
            alias="traceID_High",
            title="Trace ID High",
        ),
    ] = None
    spanID: Annotated[
        types.SpanId,
        Field(
            alias="spanID",
            title="Span ID",
        ),
    ] = None
    attributes: Annotated[
        types.Tags,
        Field(
            alias="attributes",
            title="attributes",
        ),
    ] = None
    traceState: Annotated[
        types.TraceState,
        Field(
            alias="traceState",
            title="Trace State",
        ),
    ] = None
    flags: Annotated[
        types.TraceFlags,
        Field(
            alias="flags",
            title="Flags",
        ),
    ] = None


class IntakeResolvedSpan(BaseModel):
    """
    Represents the generic information present in a span during intake.
    """

    hostname: Annotated[
        types.Hostname,
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
    ] = ...
    spanLinks: Annotated[
        List[SpanLink],
        Field(
            alias="spanLinks",
            title="Span Links",
        ),
    ] = None


class AgentPayload(BaseModel):
    """
    Represents the generic semantics for the agent payload, structurally defined here: https://github.com/DataDog/datadog-agent/blob/main/pkg/proto/datadog/trace/agent_payload.proto
    """

    hostName: Annotated[
        types.Hostname,
        Field(
            default=None,
            alias="hostName",
            title="Hostname",
            description=textwrap.dedent(
                """
                Hostname of where the agent is running."""
            ),
        ),
    ] = None
    env: Annotated[
        types.NonEmptyString,
        Field(
            alias="env",
            title="Env",
            description="""Specifies the 'env' set in the agent's configuration.""",
        ),
    ] = None
    tags: Annotated[
        Dict[str, str],
        Field(
            alias="tags",
            title="Tags",
            description="""Tags specifies tags common in all `tracerPayloads`""",
        ),
    ] = None
    agentVersion: Annotated[
        types.NonEmptyString,
        Field(
            alias="agentVersion",
            title="Agent Version",
            description="""Specifies version of the agent""",
        ),
    ] = ...
    targetTPS: Annotated[
        types.PositiveFloat,
        Field(
            alias="targetTPS",
            title="Target TPS",
            description="""Holds `TargetTPS` value in AgentConfig""",
        ),
    ] = ...
    errorTPS: Annotated[
        types.PositiveFloat,
        Field(
            alias="errorTPS",
            title="Error TPS",
            description="""Holds `ErrorTPS` value in AgentConfig""",
        ),
    ] = ...
    rareSamplerEnabled: Annotated[
        bool,
        Field(
            alias="rareSamplerEnabled",
            title="Rare Sampler Flag",
            description="""Holds `RareSamplerEnabled` value in AgentConfig""",
        ),
    ] = None

    # TODO: tracerPayloads


def generate_schema(*args, payload_type, version_info):
    json_schema_str = json.dumps(payload_type.model_json_schema(), indent=2)
    subdir = "releases" if version_info.is_release else "drafts"

    # Create the directory if it doesn't exist
    output_dir = version_info.path
    os.makedirs(output_dir, exist_ok=True)

    snake_case_name = "".join(["_" + i.lower() if i.isupper() else i for i in payload_type.__name__]).lstrip("_")

    # Write the schema to the specified file
    # output_file = os.path.join(output_dir, "schema.json")
    output_file = os.path.join(output_dir, f"{snake_case_name}.json")
    with open(output_file, "w") as f:
        f.write(json_schema_str)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate schema JSON file.")
    subparsers = parser.add_subparsers(dest="command")

    # Create the parser for the "generate" command
    generate_parser = subparsers.add_parser("generate", help="Generate something")
    generate_parser.add_argument("--release", action="store_true", help="Create a new release version")
    generate_parser.add_argument(
        "--release-type",
        choices=["major", "minor", "patch"],
        default="minor",
        nargs="?",
        const="minor",
        help="Create a new release version",
    )
    args = parser.parse_args()

    if args.command == "generate":
        latest_version_info = find_latest_version()
        new_version_info = create_new_version(latest_version_info, args.release_type, args.release)
        logger.info(f"Latest version: {latest_version_info}")
        logger.info(f"New version: {new_version_info}")

        try:
            payload_types = [IntakeResolvedSpan, IntakeResolvedHttpSpan, IntakeResolvedDbSpan, AgentPayload]

            for pt in payload_types:
                generate_schema(payload_type=pt, version_info=new_version_info)

            logger.info(f"Schema successfully generated for version: {new_version_info}")
        except Exception as e:
            logger.error(f"Error generating schema: {e}")


class VersionInfo(NamedTuple):
    version: str
    path: str
    is_release: bool

    def __str__(self):
        return f"VERSION:{self.version} PATH:{self.path} ISRELEASE:{self.is_release}"


def find_latest_version(path="./../schema/releases/", is_release=True):
    """
    Looks at all the files in the provided path. Files are of the format v{semantic_version}.

    Returns: An object with the following attributes:
        - version: The semantic version.
        - path: The path to the file.
    """
    # Ensure the path ends with a slash
    if not path.endswith("/"):
        path += "/"

    # Get all files in the directory
    files = os.listdir(path)

    # Find all files that match the format v{semantic_version}
    version_files = [f for f in files if re.match("^v\d+\.\d+\.\d+$", f)]

    # If there are no matching files, return None
    if not version_files:
        return None

    # Sort the files by semantic version
    version_files.sort(key=lambda x: [int(p) for p in x[1:].split(".")])

    # The latest file is the last one in the sorted list
    latest_file = version_files[-1]

    # Extract the semantic version and path
    version = latest_file[1:]
    full_path = os.path.abspath(path + latest_file)

    return VersionInfo(version, full_path, is_release)


def create_new_version(
    last_semantic_version: VersionInfo, semantic_version_type: str, is_release: bool
) -> VersionInfo[str, str, bool]:
    """
    Determine the next semantic version number by using the provided type (patch, minor, major), and the last semantic version.

    Args:
        semantic_version_type (str): The type of semantic version update (patch, minor, major).
        last_semantic_version (VersionInfo): The last semantic version.
        is_release (bool): Whether or not this is a release.

    Returns:
        VersionInfo: A VersionInfo with the path to the new directory and the version.
    """

    major, minor, patch = map(int, last_semantic_version.version.split("."))

    if semantic_version_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif semantic_version_type == "minor":
        minor += 1
        patch = 0
    elif semantic_version_type == "patch":
        patch += 1

    new_version = f"{major}.{minor}.{patch}"
    subdir = "releases" if is_release else "drafts"
    new_path = os.path.join("..", "schema", subdir, new_version)

    return VersionInfo(new_version, new_path, is_release)


if __name__ == "__main__":
    main()
