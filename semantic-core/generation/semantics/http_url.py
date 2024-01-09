from typing import Annotated
from pydantic import Field


HttpUrl = Annotated[
    str,
    Field(
        description="""
        The URL on an HTTP request, including the obfuscated query string.""",
        examples=["https://example.com:443/search?q=datadog"],
        min_length=1,
        json_schema_extra={"is_sensitive": True},
    ),
]
