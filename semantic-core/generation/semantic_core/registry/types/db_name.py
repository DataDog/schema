from typing import Annotated
from pydantic import Field


DbName = Annotated[
    str,
    Field(
        description="The name of the database being connected to.",
        examples=["customers"],
        json_schema_extra={"is_sensitive": False},
    ),
]
