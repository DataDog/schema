from typing import TypeVar, Type

from pydantic import Field
from typing_extensions import Annotated

T = TypeVar("T")


def prop(
    prop_type: Type[T], description: str, aspect: str, internal_description: str = None, is_internal: bool = False
):
    """
    This function produces a "property", represented as an extension of a base type (ex: int) with additional information
    that describes the property itself.

    :param prop_type: the base type of the property
    :param description: the public description of the property, to be presented to Datadog's customers
    :param internal_description:the internal description of the property, to be presented to Datadog's employees (may contain private/internal information)
    :param aspect: the aspect of the property, used to group properties together and associate them to an owner
    :param is_internal: whether the property is internal or not, hence if it should be exposed to in our public schemas or not
    """

    json_schema_extra = {
        "aspect": aspect,
        "is_internal": is_internal,
    }

    if internal_description is not None:
        json_schema_extra["internal_description"] = internal_description

    return Annotated[
        prop_type,
        Field(
            description=description,
            json_schema_extra=json_schema_extra,
        ),
    ]
