"""Functions for cleaning pandas DataFrames."""

from collections.abc import Hashable, Mapping, Sequence

import pandas as pd


def normalize_column_names(
    dataframe: pd.DataFrame, *, inplace: bool = False
) -> pd.DataFrame:
    """Convert column names to lowercase snake_case-style names.

    Spaces and hyphens become underscores, repeated underscores are collapsed,
    and leading or trailing underscores are removed.
    """
    result = dataframe if inplace else dataframe.copy()
    result.columns = [
        "_".join(
            str(column).strip().lower().replace("-", " ").replace("_", " ").split()
        )
        for column in result.columns
    ]
    return result


def remove_duplicates(
    dataframe: pd.DataFrame,
    *,
    subset: Sequence[Hashable] | None = None,
    keep: str | bool = "first",
) -> pd.DataFrame:
    """Return a new DataFrame with duplicate rows removed."""
    return dataframe.drop_duplicates(subset=subset, keep=keep).reset_index(drop=True)


def fill_missing_values(
    dataframe: pd.DataFrame, values: Mapping[Hashable, object]
) -> pd.DataFrame:
    """Fill missing values by column without changing the input DataFrame."""
    unknown_columns = set(values).difference(dataframe.columns)
    if unknown_columns:
        names = ", ".join(sorted(map(str, unknown_columns)))
        raise KeyError(f"Unknown columns: {names}")

    return dataframe.fillna(value=dict(values))


def drop_missing_rows(
    dataframe: pd.DataFrame,
    *,
    subset: Sequence[Hashable] | None = None,
    how: str = "any",
) -> pd.DataFrame:
    """Return rows that satisfy the requested missing-value rule."""
    if how not in {"any", "all"}:
        raise ValueError("how must be either 'any' or 'all'")

    return dataframe.dropna(subset=subset, how=how).reset_index(drop=True)
