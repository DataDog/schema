from typing import Annotated
from pydantic import Field


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
