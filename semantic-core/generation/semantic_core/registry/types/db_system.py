from typing import Annotated
from pydantic import Field


DbSystem = Annotated[
    str,
    Field(
        description="""An identifier for the database management system (DBMS) product being used.""",
        examples=["mysql", "postgresql"],
        pattern=r"^(adabas|buntdb|cache|cassandra|cloudscape|cockroachdb|coldfusion|consul|cosmosdb|couchbase|couchdb|db2|derby|dynamodb|edb|elasticsearch|eloquent|filemaker|firebird|firstsql|geode|h2|hanadb|hbase|hive|hsqldb|informix|ingres|instantdb|interbase|leveldb|mariadb|maxdb|memcached|mongodb|mssql|mysql|neo4j|netezza|opensearch|oracle|other_sql|pervasive|pointbase|postgresql|presto|progress|redis|redshift|snowflake|sqlite|sybase|teradata|vertica)$",
        json_schema_extra={"is_sensitive": False},
    ),
]
