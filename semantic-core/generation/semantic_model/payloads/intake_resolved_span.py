import textwrap
from typing import List
from typing_extensions import Annotated

from pydantic import BaseModel, Field

from semantic_model.registry.types import Hostname
from semantic_model.payloads.spanlinks import SpanLink


class IntakeResolvedSpan(BaseModel):
    """
    Represents the generic information present in a span during intake.
    """

    hostname: Annotated[
        Hostname,
        Field(
            alias="_dd.hostname",
            title="Hostname",
            description=textwrap.dedent(
                """
                When the DD_TRACE_REPORT_HOSTNAME=true environment variable, or report_hostname are set by the user the tracing clients will collect the hostname directly from the process or OS to report to the trace agent.
                When _dd.hostname is present the trace agent will not use it’s hostname for the trace.
                Note: this tag should only be set if configured to do so. It is disabled by default."""
            ),
        ),
    ] = ...
    spanLinks: Annotated[
        List[SpanLink],
        Field(
            alias="spanLinks",
            title="Span Links",
        ),
    ] = None
