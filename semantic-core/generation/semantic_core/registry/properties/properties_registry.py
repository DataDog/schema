from pydantic import BaseModel

from .data_policies import DataPolicies
from .is_sensitive import IsSensitive


class PropertiesRegistry(BaseModel):
    """
    Represents the registry of all Semantic Properties, i.e. the properties that can be used to define Semantic Types.
    """

    is_sensitive: IsSensitive
    data_policies: DataPolicies
