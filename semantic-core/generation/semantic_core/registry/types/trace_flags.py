from typing_extensions import Annotated
from pydantic import Field


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
