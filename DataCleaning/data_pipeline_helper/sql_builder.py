"""Small parameterized SQL builders.

Values are returned separately from SQL text to discourage unsafe string
interpolation. Table and column identifiers are validated before use.
"""

from collections.abc import Mapping, Sequence
import re
from typing import Any

_IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _validate_identifier(identifier: str) -> str:
    if not isinstance(identifier, str) or not _IDENTIFIER_PATTERN.fullmatch(identifier):
        raise ValueError(f"Invalid SQL identifier: {identifier!r}")
    return identifier


def _validated_columns(columns: Sequence[str]) -> list[str]:
    if not columns:
        raise ValueError("At least one column is required")
    return [_validate_identifier(column) for column in columns]


def build_insert(
    table: str,
    data: Mapping[str, Any],
    *,
    placeholder: str = "%s",
) -> tuple[str, tuple[Any, ...]]:
    """Build a parameterized INSERT statement and its ordered values."""
    table_name = _validate_identifier(table)
    columns = _validated_columns(list(data))
    if not placeholder:
        raise ValueError("placeholder cannot be empty")

    column_sql = ", ".join(columns)
    placeholder_sql = ", ".join([placeholder] * len(columns))
    sql = f"INSERT INTO {table_name} ({column_sql}) VALUES ({placeholder_sql})"
    return sql, tuple(data[column] for column in columns)


def build_select(
    table: str,
    *,
    columns: Sequence[str] | None = None,
    where: Mapping[str, Any] | None = None,
    placeholder: str = "%s",
) -> tuple[str, tuple[Any, ...]]:
    """Build a parameterized SELECT statement with equality filters."""
    table_name = _validate_identifier(table)
    if not placeholder:
        raise ValueError("placeholder cannot be empty")
    selected_columns = "*" if columns is None else ", ".join(_validated_columns(columns))
    sql = f"SELECT {selected_columns} FROM {table_name}"
    parameters: tuple[Any, ...] = ()

    if where:
        where_columns = _validated_columns(list(where))
        conditions = " AND ".join(
            f"{column} = {placeholder}" for column in where_columns
        )
        sql = f"{sql} WHERE {conditions}"
        parameters = tuple(where[column] for column in where_columns)

    return sql, parameters
