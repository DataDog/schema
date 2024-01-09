from typing import Annotated
from pydantic import Field


DbOperation = Annotated[
    str,
    Field(
        description="The name of the operation being executed, e.g. the MongoDB command name such as findAndModify, or the SQL keyword.",
        examples=["findAndModify", "HMSET", "SELECT"],
        json_schema_extra={"is_sensitive": False},
    ),
]
