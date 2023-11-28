import json
import logging
import os
import textwrap

from pydantic import BaseModel, Field
from typing_extensions import Annotated

# Semantic Types

Hostname = Annotated[
    str,
    Field(
        description="""
        A hostname is a label that is assigned to a device connected to a computer network and that is used to identify the device in various forms of electronic communication, such as the World Wide Web.
        An empty hostname is a valid value and it signals that Datadog has been able to explicitly collect that no hostname was available when the client side data was produced. This is different from a hostname not being available in a given payload, which signals that there may or may not have been a hostname available, but that data was simply not collected.""",
        examples=["my-hostname"],
        min_length=0,
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
            An IP address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.
            We support both IPv4 and IPv6 addresses."""
        ),
        examples=["192.168.123.132"],
        pattern=r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}|(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$",
        json_schema_extra={"is_sensitive": True},
    ),
]

DbSystem = Annotated[
    str,
    Field(
        description="""An identifier for the database management system (DBMS) product being used.""",
        examples=["mysql", "postgresql"],
        pattern=r"^(adabas|buntdb|cache|cassandra|cloudscape|cockroachdb|coldfusion|consul|cosmosdb|couchbase|couchdb|db2|derby|dynamodb|edb|elasticsearch|eloquent|filemaker|firebird|firstsql|geode|h2|hanadb|hbase|hive|hsqldb|informix|ingres|instantdb|interbase|leveldb|mariadb|maxdb|memcached|mongodb|mssql|mysql|neo4j|netezza|opensearch|oracle|other_sql|pervasive|pointbase|postgresql|presto|progress|redis|redshift|snowflake|sqlite|sybase|teradata|vertica)$",
        json_schema_extra={"is_sensitive": False},
    ),
]

DbConnectionString = Annotated[
    str,
    Field(
        description="The connection string used to connect to the database.",
        examples=["Server=(localdb)\v11.0;Integrated Security=true;","postgresql://localhost:5432"],
        json_schema_extra={"is_sensitive": True},
    ),
]

DbUser = Annotated[
    str,
    Field(
        description="Username for accessing the database.",
        examples="widget_user",
        json_schema_extra={"is_sensitive": False},
    ),
]

DbName = Annotated[
    str,
    Field(
        description="The name of the database being connected to.",
        examples="customers",
        json_schema_extra={"is_sensitive": False},
    ),
]

DbStatement = Annotated[
    str,
    Field(
        description="The database statement being executed.",
        examples="""SELECT * FROM wuser_table', 'SET mykey "WuValue""",
        json_schema_extra={"is_sensitive": True},
    ),
]

DbOperation = Annotated[
    str,
    Field(
        description="The name of the operation being executed, e.g. the MongoDB command name such as findAndModify, or the SQL keyword.",
        examples=["findAndModify", "HMSET", "SELECT"],
        json_schema_extra={"is_sensitive": False},
    ),
]

DbSqlTable = Annotated[
    str,
    Field(
        description="The name of the primary table that the operation is acting upon, including the database name (if applicable).",
        examples=["customers"],
        json_schema_extra={"is_sensitive": False},
    ),
]

DbRowCount = Annotated[
    int,
    Field(
        description=textwrap.dedent("""
                                    The number of rows/results from the query or operation. For caches and other datastores, i.e. Redis, this tag should only set for operations that retrieve stored data,
                                    such as GET operations and queries, excluding SET and other commands not returning data. """),
        examples=["customers"],
        ge=0,
        json_schema_extra={"is_sensitive": False},
    ),
]

# Semantic Models


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

class IntakeResolvedDbSpan(BaseModel):
    """
    Semantic model for the DB information present in a span during intake.
    """
    db_system: Annotated[
        DbSystem,
        Field(
            alias="db.system",
            title="DB System",
            description=DbSystem.__metadata__[0].description
        )
    ] = ...
    db_connection_string: Annotated[
        DbConnectionString,
        Field(
            alias="db.connection_string",
            title="DB Connection String",
            description=DbConnectionString.__metadata__[0].description
        )
    ] = None
    db_user: Annotated[
        DbUser,
        Field(
            alias="db.user",
            title="DB User",
            description=DbUser.__metadata__[0].description
        )
    ] = None
    db_name: Annotated[
        DbName,
        Field(
            alias="db.name",
            title="DB Name",
            description=DbName.__metadata__[0].description
        )
    ] = None
    db_statement: Annotated[
        DbStatement,
        Field(
            alias="db.statement",
            title="DB Statement",
            description=DbStatement.__metadata__[0].description
        )
    ] = None
    db_operation: Annotated[
        DbOperation,
        Field(
            alias="db.operation",
            title="DB Operation",
            description=DbOperation.__metadata__[0].description
        )
    ] = None
    db_sql_table: Annotated[
        DbSqlTable,
        Field(
            alias="db.sql.table",
            title="DB SQL Table",
            description=DbSqlTable.__metadata__[0].description
        )
    ] = None
    db_row_count: Annotated[
        DbRowCount,
        Field(
            alias="db.row_count",
            title="DB Row Count",
            description=DbRowCount.__metadata__[0].description
        )
    ] = None


class IntakeResolvedSpan(BaseModel):
    """
    Represents the generic information present in a span during intake.
    """

    hostname: Annotated[
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
    ] = ...


class AgentPayload(BaseModel):
    """
    Represents the generic semantics for the agent payload, structurally defined here: https://github.com/DataDog/datadog-agent/blob/main/pkg/proto/datadog/trace/agent_payload.proto
    """

    hostName: Annotated[
        Hostname,
        Field(
            default=None,
            alias="hostName",
            title="Hostname",
            description=textwrap.dedent(
                """
                Hostname of where the agent is running."""
            ),
        ),
    ] = ...


def generate_schema(payload_type, version):

    json_schema_str = json.dumps(payload_type.model_json_schema(), indent=2)

    # Create the directory if it doesn't exist
    output_dir = os.path.join(os.getcwd(), version)
    os.makedirs(output_dir, exist_ok=True)

    snake_case_name = "".join(
        ["_" + i.lower() if i.isupper() else i for i in payload_type.__name__]
    ).lstrip("_")

    # Write the schema to the specified file
    # output_file = os.path.join(output_dir, "schema.json")
    output_file = os.path.join(output_dir, f"{snake_case_name}.json")
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
        payload_types = [IntakeResolvedSpan, IntakeResolvedHttpSpan, IntakeResolvedDbSpan, AgentPayload]

        for pt in payload_types:
            generate_schema(pt, version=args.version)

        logger.info(f"Schema successfully generated for version: {args.version}")
    except Exception as e:
        logger.error(f"Error generating schema: {e}")
