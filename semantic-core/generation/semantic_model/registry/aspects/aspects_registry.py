from pydantic import BaseModel

from .infosec import InfoSec


class AspectsRegistry(BaseModel):
    """
    Represents the registry of all Semantic Aspects, i.e. the groups of properties that are related to each other and
    are curated by one owner.
    """

    infosec: InfoSec
