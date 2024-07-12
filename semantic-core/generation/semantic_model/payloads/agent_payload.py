from pydantic import BaseModel, Field
import textwrap
from typing_extensions import Annotated
from typing import List, Dict

from semantic_model.registry.types import Hostname
from semantic_model.registry.types.span import Span
from semantic_model.registry.types.span_type import SpanType
from semantic_model.registry.types.tags_base import TagsBase
from semantic_model.registry.types.tags_http import TagsHTTP
from semantic_model.registry.types.tags_sql import TagsSQL
from semantic_model.registry.types.tracer_payload import TracerPayload

NonEmptyString = Annotated[str, Field(min_length=1)]
PositiveFloat = Annotated[float, Field(gt=0)]


class AgentPayload(BaseModel):
    """
    Represents the generic semantic_model for the agent payload, structurally defined here: https://github.com/DataDog/datadog-agent/blob/main/pkg/proto/datadog/trace/agent_payload.proto
    """

    @staticmethod
    def customize_json_schema(schema):
        if '$defs' not in schema:
            schema['$defs'] = {}

        extra_models = [TagsBase, TagsHTTP, TagsSQL]

        # generate the JSON schema for the extra models and add it to the root definitions.
        for cls in extra_models:
            name = cls.__name__
            schema['$defs'][name] = cls.model_json_schema()

        span_type = 'type'

        # Validate the span.meta property using different schemas conditionally, based on
        # the span.type attribute.
        # https://json-schema.org/understanding-json-schema/reference/conditionals#ifthenelse
        # This feature is not supported by Pydantic: https://github.com/pydantic/pydantic/issues/529
        schema['$defs'][Span.__name__]['allOf'] = [
            # default case when type is not defined or is not a known value
            {
                'if': {'not': {'properties': {span_type: {'enum': [SpanType.web, SpanType.http, SpanType.sql]}}}},
                'then': {'properties': {'meta': {'$ref': f"#/$defs/{TagsBase.__name__}"}}}
            },
            {
                'if': {
                    'properties': {span_type: {'enum': [SpanType.web, SpanType.http]}},
                    'required': [span_type]
                },
                'then': {'properties': {'meta': {'$ref': f"#/$defs/{TagsHTTP.__name__}"}}},
            },
            {
                'if': {
                    'properties': {span_type: {'const': SpanType.sql}},
                    'required': [span_type]
                },
                'then': {'properties': {'meta': {'$ref': f"#/$defs/{TagsSQL.__name__}"}}},
            },
        ]

        # Move the nested $defs to the root model, so the generated references still work.
        for cls in extra_models:
            name = cls.__name__
            schema['$defs'] = schema['$defs'] | schema['$defs'][name]['$defs']
            del schema['$defs'][name]['$defs']

        return schema

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
    tracerPayloads: Annotated[
        List[TracerPayload],
        Field(
            alias="tracerPayloads",
            title="Tracer Payloads",
            description="""Specifies the list of the payloads received from tracers""",
        )
    ]
