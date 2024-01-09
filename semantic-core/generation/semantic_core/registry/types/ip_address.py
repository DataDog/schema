from typing import Annotated
from pydantic import Field
import textwrap


IpAddress = Annotated[
    str,
    Field(
        description=textwrap.dedent(
            """
            An IP address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.
            We support both IPv4 and IPv6 addresses."""
        ),
        examples=["192.168.123.132"],
        pattern=r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}|(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$",
        json_schema_extra={"is_sensitive": True},
    ),
]
