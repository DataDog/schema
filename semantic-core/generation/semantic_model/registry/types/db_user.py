from typing import Annotated
from pydantic import Field


DbUser = Annotated[
    str,
    Field(
        description="Username for accessing the database.",
        examples=["widget_user"],
        json_schema_extra={"is_sensitive": False},
    ),
]
