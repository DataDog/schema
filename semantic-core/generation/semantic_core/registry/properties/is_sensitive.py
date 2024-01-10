from .util import prop

IsSensitive = prop(
    prop_type=bool,
    description="""Indicates if the field associated with this property contains sensitive data or not.""",
    internal_description="""Sensitive data has some implications that T&S must define.""",
    aspect="security",
)
