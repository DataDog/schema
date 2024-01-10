from enum import Enum

from .util import prop


class PoliciesEnum(str, Enum):
    GDPR = "GDPR"
    CCPA = "CCPA"
    HIPAA = "HIPAA"


DataPolicies = prop(
    prop_type=list[PoliciesEnum],
    description="""A list of data policies that apply to the associated field.""",
    aspect="security",
)
