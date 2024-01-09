import textwrap
from typing import Annotated
from pydantic import Field


DbRowCount = Annotated[
    int,
    Field(
        description=textwrap.dedent(
            """
                                    The number of rows/results from the query or operation. For caches and other datastores, i.e. Redis, this tag should only set for operations that retrieve stored data,
                                    such as GET operations and queries, excluding SET and other commands not returning data. """
        ),
        examples=["customers"],
        ge=0,
        json_schema_extra={"is_sensitive": False},
    ),
]
