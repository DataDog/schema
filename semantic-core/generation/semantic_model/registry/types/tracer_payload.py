from pydantic import BaseModel, Field
from typing_extensions import Annotated
from typing import List

from semantic_model.registry.types.language_name import LanguageName
from semantic_model.registry.types.trace_chunk import TraceChunk


class TracerPayload(BaseModel):
    containerID: Annotated[
        str,
        Field(
            alias="containerID",
            title="Container ID",
            description="Specifies the ID of the container where the tracer is running on"
        )
    ] = None
    languageName: Annotated[
        LanguageName,
        Field(
            alias="languageName",
            title="Language Name",
            description="Specifies the language of the tracer",
        )
    ]
    languageVersion: Annotated[
        str,
        Field(
            alias="languageVersion",
            title="Language Version",
            description="Specifies the language version of the tracer",
            # TODO: add pattern to validate version string
        )
    ]
    tracerVersion: Annotated[
        str,
        Field(
            alias="tracerVersion",
            title="Tracer Version",
            description="Specifies the version of the tracer",
            # TODO: add pattern to validate version string
        )
    ]
    runtimeID: Annotated[
        str,
        Field(
            alias="runtimeID",
            title="Runtime ID",
            description="Specifies V4 UUID representation of a tracer session",
            # TODO: add pattern to validate UUID
        )
    ] = None
    chunks: Annotated[
        List[TraceChunk],
        Field(
            alias="chunks",
            title="Trace Chunks",
            description="Specifies the list of containing trace chunks",
        )
    ]
    tags: Annotated[
        dict[str, str],
        Field(
            alias="tags",
            title="Trace Tags",
            description="Specifies the list of tags common in all Trace Chunks",
        )
    ] = None
    env: Annotated[
        str,
        Field(
            alias="env",
            title="Env",
            description="Specifies the `env` tag that is set in the tracer configuration",
        )
    ]
    hostname: Annotated[
        str,
        Field(
            alias="hostname",
            title="Hostname",
            description="Specifies the hostname where the tracer is running",
        )
    ] = None
    appVersion: Annotated[
        str,
        Field(
            alias="appVersion",
            title="App Version",
            description="Specifies the `version` tag that set in the tracer configuration",
        )
    ]
