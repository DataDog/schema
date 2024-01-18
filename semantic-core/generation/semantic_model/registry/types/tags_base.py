from pydantic import BaseModel, Field

from typing_extensions import Annotated

from semantic_model.registry.types.span_kind import SpanKind


class TagsBase(BaseModel):
    span_kind: Annotated[
        SpanKind,
        Field(
            alias="span.kind",
            title="span.kind",
            description="",
        )
    ]
