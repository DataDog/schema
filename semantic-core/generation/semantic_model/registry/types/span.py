from pydantic import BaseModel, Field
from typing_extensions import Annotated

from semantic_model.registry.types import SpanId
from semantic_model.registry.types.span_type import SpanType


class Span(BaseModel):
    service: Annotated[
        str,
        Field(
            alias="service",
            title="Service",
            description="The name of the service with which this span is associated"
        )
    ]
    name: Annotated[
        str,
        Field(
            alias="name",
            title="Name",
            description="The operation name of this span"
        )
    ]
    resource: Annotated[
        str,
        Field(
            alias="resource",
            title="Resource",
            description="The resource name of this span, also sometimes called the endpoint (for web spans)"
        )
    ]
    traceID: Annotated[
        str,
        Field(
            alias="traceID",
            title="Trace ID",
            description="The ID of the trace to which this span belongs"
        )
    ]
    spanID: Annotated[
        SpanId,
        Field(
            alias="spanID",
            title="Span ID",
        ),
    ] = None
    parentID: Annotated[
        SpanId,
        Field(
            alias="parentID",
            title="Parent ID",
            description="The ID of this span's parent, or zero if this span has no parent"
        )
    ] = None
    start: Annotated[
        int,
        Field(
            alias="start",
            title="Start",
            description="The number of nanoseconds between the Unix epoch and the beginning of this span"
        )
    ]
    duration: Annotated[
        int,
        Field(
            alias="duration",
            title="Duration",
            description="The time length of this span in nanoseconds"
        )
    ]
    error: Annotated[
        int,
        Field(
            alias="error",
            title="Error",
            description="Error is 1 if there is an error associated with this span, or 0 if there is not"
        )
    ] = None
    meta: Annotated[
        dict[str, str],
        Field(
            alias="meta",
            title="Meta",
            description="Meta is a mapping from tag name to tag value for string-valued tags"
        )
    ] = None
    metrics: Annotated[
        dict[str, float],
        Field(
            alias="metrics",
            title="Metrics",
            description="Metrics is a mapping from tag name to tag value for numeric-valued tags"
        )
    ] = None
    type: Annotated[
        SpanType,
        Field(
            alias="type",
            title="Type",
            description="Represents the type of the service with which this span is associated. Example values: `web`, `db`, `lambda`"
        )
    ] = None
    meta_struct: Annotated[
        dict[str, int],
        Field(
            alias="meta_struct",
            title="Meta Struct",
            description="Represents a registry of structured \"other\" data used by, e.g., AppSec"
        )
    ] = None
