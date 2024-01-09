from typing import Annotated
from pydantic import Field


HttpRoute = Annotated[
    str,
    Field(
        description="""
        The matched route (path template) of an HTTP request.""",
        examples=["/users/:userID"],
        min_length=1,
        json_schema_extra={"is_sensitive": False},
    ),
]
