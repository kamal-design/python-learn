"""Reusable helpers for small data-cleaning and ETL pipelines."""

from .cleaning import (
    drop_missing_rows,
    fill_missing_values,
    normalize_column_names,
    remove_duplicates,
)
from .etl import extract_csv, load_csv, run_csv_pipeline, transform_data
from .sql_builder import build_insert, build_select
from .utils import validate_required_columns

__version__ = "0.1.0"

__all__ = [
    "build_insert",
    "build_select",
    "drop_missing_rows",
    "extract_csv",
    "fill_missing_values",
    "load_csv",
    "normalize_column_names",
    "remove_duplicates",
    "run_csv_pipeline",
    "transform_data",
    "validate_required_columns",
]
