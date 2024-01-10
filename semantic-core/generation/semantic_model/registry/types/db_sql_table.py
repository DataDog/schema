from typing import Annotated
from pydantic import Field


DbSqlTable = Annotated[
    str,
    Field(
        description="The name of the primary table that the operation is acting upon, including the database name (if applicable).",
        examples=["customers"],
        json_schema_extra={"is_sensitive": False},
    ),
]
