from pydantic import BaseModel, Field
from typing_extensions import Annotated
from typing import List

from semantic_model.registry.types.span import Span


class TraceChunk(BaseModel):
    priority: Annotated[
        int,
        Field(
            alias="priority",
            title="Priority",
            description="Specifies the sampling priority of the trace"
        )
    ]
    origin: Annotated[
        str,
        Field(
            alias="origin",
            title="Origin",
            description="Specifies the origin product (`lambda`, `rum`, etc.) of the trace"
        )
    ] = None
    spans: Annotated[
        List[Span],
        Field(
            alias="spans",
            title="Spans",
            description="Specifies the list of containing spans"
        )
    ]
    tags: Annotated[
        dict[str, str],
        Field(
            alias="tags",
            title="Tags",
            description="Specifies the list of tags common in all Spans",
        )
    ] = None
    droppedTrace: Annotated[
        bool,
        Field(
            alias="droppedTrace",
            title="Dropped Trace",
            description="Specifies whether the trace was dropped by samplers or not",
        )
    ] = None
