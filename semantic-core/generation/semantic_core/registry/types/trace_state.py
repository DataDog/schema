from typing_extensions import Annotated
from pydantic import Field


TraceState = Annotated[
    str,
    Field(
        description="""
        Additional vendor-specific trace identification information across different distributed tracing systems. The tracestate field may contain any opaque value in any of the keys. See https://www.w3.org/TR/trace-context/#tracestate-header.""",
        examples=["rojo=00f067aa0ba902b7", "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE"],
        json_schema_extra={"is_sensitive": False},
    ),
]