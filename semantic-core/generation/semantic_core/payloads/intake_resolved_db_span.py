import textwrap
from typing import Annotated
from pydantic import Field, BaseModel

from semantic_core.registry.types import DbSystem
from semantic_core.registry.types import DbUser
from semantic_core.registry.types import DbName
from semantic_core.registry.types import DbStatement
from semantic_core.registry.types import DbOperation
from semantic_core.registry.types import DbSqlTable
from semantic_core.registry.types import DbRowCount
from semantic_core.registry.types import DbConnectionString


class IntakeResolvedDbSpan(BaseModel):
    """
    Semantic model for the DB information present in a span during intake.
    """

    db_system: Annotated[
        DbSystem,
        Field(
            alias="db.system",
            title="DB System",
        ),
    ] = ...
    db_connection_string: Annotated[
        DbConnectionString,
        Field(
            alias="db.connection_string",
            title="DB Connection String",
        ),
    ] = None
    db_user: Annotated[
        DbUser,
        Field(
            alias="db.user",
            title="DB User",
        ),
    ] = None
    db_name: Annotated[
        DbName,
        Field(
            alias="db.name",
            title="DB Name",
        ),
    ] = None
    db_statement: Annotated[
        DbStatement,
        Field(
            alias="db.statement",
            title="DB Statement",
        ),
    ] = None
    db_operation: Annotated[
        DbOperation,
        Field(
            alias="db.operation",
            title="DB Operation",
        ),
    ] = None
    db_sql_table: Annotated[
        DbSqlTable,
        Field(
            alias="db.sql.table",
            title="DB SQL Table",
        ),
    ] = None
    db_row_count: Annotated[
        DbRowCount,
        Field(
            alias="db.row_count",
            title="DB Row Count",
        ),
    ] = None
