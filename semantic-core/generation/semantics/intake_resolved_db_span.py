import textwrap
from typing import Annotated
from pydantic import Field, BaseModel

from semantics.db_system import DbSystem
from semantics.db_user import DbUser
from semantics.db_name import DbName
from semantics.db_statement import DbStatement
from semantics.db_operation import DbOperation
from semantics.db_sql_table import DbSqlTable
from semantics.db_row_count import DbRowCount
from semantics.db_connection_string import DbConnectionString


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
