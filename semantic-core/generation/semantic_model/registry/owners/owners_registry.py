from pydantic import BaseModel

from .trust_and_safety import TrustAndSafety


class OwnersRegistry(BaseModel):
    """
    Represents the registry of all Semantic Owners, i.e. the owners that maintain Semantic Properties.
    """

    trust_and_safety: TrustAndSafety
