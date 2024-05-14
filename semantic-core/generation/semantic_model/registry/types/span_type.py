from enum import Enum


class SpanType(str, Enum):
    """Span types have similar behaviour to "app types" and help categorize
    traces in the Datadog application. They can also help fine grain agent
    level behaviours such as obfuscation and quantization, when these are
    enabled in the agent's configuration."""

    web = 'web'
    http = 'http'
    sql = 'sql'
    cassandra = 'cassandra'
    redis = 'redis'
    memcached = 'memcached'
    mongodb = 'mongodb'
    elasticsearch = 'elasticsearch'
    leveldb = 'leveldb'
    dns = 'dns'
    queue = 'queue'
    consul = 'consul'
    graphql = 'graphql'
