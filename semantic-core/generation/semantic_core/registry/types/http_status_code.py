from typing import Annotated
from pydantic import Field


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
