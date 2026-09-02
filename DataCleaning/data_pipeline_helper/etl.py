"""Extract, transform, and load helpers for CSV pipelines."""

from collections.abc import Hashable, Mapping, Sequence
from pathlib import Path
from typing import Any

import pandas as pd

from .cleaning import fill_missing_values, normalize_column_names, remove_duplicates
from .utils import ensure_parent_directory, validate_required_columns


def extract_csv(file_path: str | Path, **read_csv_options: Any) -> pd.DataFrame:
    """Extract data from a CSV file into a DataFrame."""
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"CSV input file does not exist: {path}")
    return pd.read_csv(path, **read_csv_options)


def transform_data(
    dataframe: pd.DataFrame,
    *,
    fill_values: Mapping[Hashable, object] | None = None,
    required_columns: Sequence[Hashable] | None = None,
    normalize_columns: bool = True,
    deduplicate: bool = True,
) -> pd.DataFrame:
    """Apply common cleaning steps and return a new DataFrame.

    Required columns are checked after column-name normalization. Therefore,
    use normalized names such as ``customer_name`` when normalization is on.
    """
    result = dataframe.copy()
    if normalize_columns:
        result = normalize_column_names(result)
    if required_columns:
        validate_required_columns(result, required_columns)
    if fill_values:
        result = fill_missing_values(result, fill_values)
    if deduplicate:
        result = remove_duplicates(result)
    return result


def load_csv(
    dataframe: pd.DataFrame,
    file_path: str | Path,
    *,
    index: bool = False,
    **to_csv_options: Any,
) -> Path:
    """Load a DataFrame into a CSV file and return the output path."""
    path = ensure_parent_directory(file_path)
    dataframe.to_csv(path, index=index, **to_csv_options)
    return path


def run_csv_pipeline(
    input_file: str | Path,
    output_file: str | Path,
    *,
    fill_values: Mapping[Hashable, object] | None = None,
    required_columns: Sequence[Hashable] | None = None,
    normalize_columns: bool = True,
    deduplicate: bool = True,
) -> pd.DataFrame:
    """Run extract, transform, and load steps for one CSV file."""
    extracted = extract_csv(input_file)
    transformed = transform_data(
        extracted,
        fill_values=fill_values,
        required_columns=required_columns,
        normalize_columns=normalize_columns,
        deduplicate=deduplicate,
    )
    load_csv(transformed, output_file)
    return transformed
