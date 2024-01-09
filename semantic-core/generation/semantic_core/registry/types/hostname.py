from pydantic import Field
from typing_extensions import Annotated


Hostname = Annotated[
    str,
    Field(
        description="""
        A hostname is a label that is assigned to a device connected to a computer network and that is used to identify the device in various forms of electronic communication, such as the World Wide Web.
        An empty hostname is a valid value and it signals that Datadog has been able to explicitly collect that no hostname was available when the client side data was produced. This is different from a hostname not being available in a given payload, which signals that there may or may not have been a hostname available, but that data was simply not collected.""",
        examples=["my-hostname"],
        min_length=0,
        json_schema_extra={"is_sensitive": False},
    ),
]
