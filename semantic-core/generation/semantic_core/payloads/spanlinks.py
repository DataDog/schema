from typing_extensions import Annotated
from typing import List, Dict
from pydantic import BaseModel, Field

from semantic_core.registry.types import TraceId, SpanId, Tags, TraceState, TraceFlags


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
