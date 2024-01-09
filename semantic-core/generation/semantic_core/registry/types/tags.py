from typing_extensions import Annotated
from pydantic import Field
from typing import Dict


Tags = Annotated[
    Dict,
    Field(
        description="""
        This field represents an arbitrary map of key-value pairs.""",
        examples=[{"foo": "bar", "key": "value"}],
        json_schema_extra={"is_sensitive": False},
    ),
]