import textwrap
from typing import Annotated
from typing import TypeVar, Type

from pydantic import Field

T = TypeVar("T")


def signal(signal_type: Type[T], description: str):
    """
    This function produces a "signal", represented as an extension of a base type (ex: int) with additional information.
    Signals are meant to be used as part of the definition of complex validations.

    :param signal_type: The type of the signal.
    :param description: The description of the signal.
    """

    return Annotated[
        signal_type,
        Field(description=textwrap.dedent(description).lstrip()),
    ]
