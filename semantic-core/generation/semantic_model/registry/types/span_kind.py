from enum import Enum


class SpanKind(str, Enum):
    internal = 'internal'
    client = 'client'
    server = 'server'
    producer = 'producer'
    consumer = 'consumer'
