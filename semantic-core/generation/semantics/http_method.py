from typing import Annotated
from pydantic import Field


HttpMethod = Annotated[
    str,
    Field(
        description="""
        The HTTP method used for the connection. Required for both client and server spans.""",
        examples=["GET", "POST", "PUT", "DELETE", "PATCH"],
        pattern=r"^(GET|HEAD|POST|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)$",
        json_schema_extra={"is_sensitive": False},
    ),
]
