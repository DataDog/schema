from typing import Annotated
from pydantic import Field


HttpUserAgent = Annotated[
    str,
    Field(
        description="""
        The user agent header received with the request.""",
        examples=["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"],
        min_length=1,
        json_schema_extra={"is_sensitive": True},
    ),
]
