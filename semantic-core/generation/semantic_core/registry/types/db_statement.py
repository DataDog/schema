from typing import Annotated
from pydantic import Field


DbStatement = Annotated[
    str,
    Field(
        description="The database statement being executed.",
        examples=["""SELECT * FROM wuser_table', 'SET mykey "WuValue"""],
        json_schema_extra={"is_sensitive": True},
    ),
]
