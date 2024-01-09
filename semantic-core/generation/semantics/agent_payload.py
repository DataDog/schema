from pydantic import BaseModel, Field
import textwrap
from typing_extensions import Annotated
from typing import List, Dict

from semantics.hostname import Hostname


NonEmptyString = Annotated[str, Field(min_length=1)]
PositiveFloat = Annotated[float, Field(gt=0)]


class AgentPayload(BaseModel):
    """
    Represents the generic semantics for the agent payload, structurally defined here: https://github.com/DataDog/datadog-agent/blob/main/pkg/proto/datadog/trace/agent_payload.proto
    """

    hostName: Annotated[
        Hostname,
        Field(
            default=None,
            alias="hostName",
            title="Hostname",
            description=textwrap.dedent(
                """
                Hostname of where the agent is running."""
            ),
        ),
    ] = None
    env: Annotated[
        NonEmptyString,
        Field(
            alias="env",
            title="Env",
            description="""Specifies the 'env' set in the agent's configuration.""",
        ),
    ] = None
    tags: Annotated[
        Dict[str, str],
        Field(
            alias="tags",
            title="Tags",
            description="""Tags specifies tags common in all `tracerPayloads`""",
        ),
    ] = None
    agentVersion: Annotated[
        NonEmptyString,
        Field(
            alias="agentVersion",
            title="Agent Version",
            description="""Specifies version of the agent""",
        ),
    ] = ...
    targetTPS: Annotated[
        PositiveFloat,
        Field(
            alias="targetTPS",
            title="Target TPS",
            description="""Holds `TargetTPS` value in AgentConfig""",
        ),
    ] = ...
    errorTPS: Annotated[
        PositiveFloat,
        Field(
            alias="errorTPS",
            title="Error TPS",
            description="""Holds `ErrorTPS` value in AgentConfig""",
        ),
    ] = ...
    rareSamplerEnabled: Annotated[
        bool,
        Field(
            alias="rareSamplerEnabled",
            title="Rare Sampler Flag",
            description="""Holds `RareSamplerEnabled` value in AgentConfig""",
        ),
    ] = None

    # TODO: tracerPayloads
