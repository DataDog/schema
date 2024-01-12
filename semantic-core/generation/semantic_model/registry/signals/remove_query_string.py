from .util import signal

RemoveQueryString = signal(
    signal_type=bool,
    description="""
    True if the agent that sent a payload containing an http url is configured to remove the query string from the url before sending it to the backend.
    See: https://docs.datadoghq.com/tracing/configure_data_security/?tab=http
    """,
)
