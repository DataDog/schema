from typing_extensions import Annotated
from typing import List, Dict
from pydantic import BaseModel, Field

from semantics.traces import TraceId, SpanId, Tags, TraceState


TraceFlags = Annotated[
    int,
    Field(
        description="""
        An 32-bit integer that controls tracing flags such as sampling, trace level, etc. These flags are recommendations given by the caller rather than strict rules to follow. Flags may include zero as valid value. The 31th bit must thus be set to distinguish unset vs zero value.""",
        ge=0,
        le=0xFFFFFFFF,
        examples=[0, 4, 128, 4294967296],
        json_schema_extra={"is_sensitive": False},
    ),
]

Tags = Annotated[
    Dict,
    Field(
        description="""
        This field represents an arbitrary map of key-value pairs.""",
        examples=[{"foo": "bar", "key": "value"}],
        json_schema_extra={"is_sensitive": False},
    ),
]


class SpanLink(BaseModel):
    traceID: Annotated[
        TraceId,
        Field(
            alias="traceID",
            title="Trace ID",
        ),
    ] = ...
    traceID_High: Annotated[
        TraceId,
        Field(
            alias="traceID_High",
            title="Trace ID High",
        ),
    ] = None
    spanID: Annotated[
        SpanId,
        Field(
            alias="spanID",
            title="Span ID",
        ),
    ] = None
    attributes: Annotated[
        Tags,
        Field(
            alias="attributes",
            title="attributes",
        ),
    ] = None
    traceState: Annotated[
        TraceState,
        Field(
            alias="traceState",
            title="Trace State",
        ),
    ] = None
    flags: Annotated[
        TraceFlags,
        Field(
            alias="flags",
            title="Flags",
        ),
    ] = None
