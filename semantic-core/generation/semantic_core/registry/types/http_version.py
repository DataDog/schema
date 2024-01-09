from typing import Annotated
from pydantic import Field


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
