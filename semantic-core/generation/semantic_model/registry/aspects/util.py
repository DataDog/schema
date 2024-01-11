from typing import Annotated

from pydantic import Field


def aspect(id: str, owner: str, description: str):
    json_schema_extra = {
        "id": id,
        "owner": owner,
    }

    return Annotated[
        str,
        Field(description=description, json_schema_extra=json_schema_extra),
    ]
