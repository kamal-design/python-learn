"""Utility helpers shared by package modules."""

from collections.abc import Hashable, Sequence
from pathlib import Path

import pandas as pd


def ensure_parent_directory(file_path: str | Path) -> Path:
    """Create an output file's parent directories and return its Path."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def validate_required_columns(
    dataframe: pd.DataFrame, required_columns: Sequence[Hashable]
) -> None:
    """Raise ValueError when one or more required columns are absent."""
    missing = [column for column in required_columns if column not in dataframe.columns]
    if missing:
        names = ", ".join(map(str, missing))
        raise ValueError(f"Missing required columns: {names}")
