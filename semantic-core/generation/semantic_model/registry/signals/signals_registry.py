from pydantic import BaseModel

from .remove_query_string import RemoveQueryString


class SignalsRegistry(BaseModel):
    """
    Represents the registry of all signals that can be used to define complex validations.
    """

    remove_query_string: RemoveQueryString
