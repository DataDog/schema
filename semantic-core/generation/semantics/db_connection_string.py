from typing import Annotated
from pydantic import Field


DbConnectionString = Annotated[
    str,
    Field(
        description="The connection string used to connect to the database.",
        examples=["Server=(localdb)\v11.0;Integrated Security=true;", "postgresql://localhost:5432"],
        json_schema_extra={"is_sensitive": True},
    ),
]
