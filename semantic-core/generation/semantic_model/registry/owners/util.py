from typing import Annotated

from pydantic import Field


def owner(id: str, team: str, description: str, contacts: list[str]):
    json_schema_extra = {
        "id": id,
        "team": team,
        "contacts": contacts,
    }

    return Annotated[
        str,
        Field(description=description, json_schema_extra=json_schema_extra),
    ]
