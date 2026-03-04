import csv
import numpy as np
from pathlib import Path
from typing import List, Dict

def load_covid_data(filepath: str | Path) -> List[Dict[str, str]]:
    """
    Loads the Ontario COVID hospital/ICU CSV into a list of dictionaries.
    Uses csv.DictReader — keeps everything as string initially.
    """
    filepath = Path(filepath)
    if not filepath.is_file():
        raise FileNotFoundError(f"Data file not found: {filepath}")

    data = []
    with filepath.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def extract_column(data: List[Dict[str, str]], column: str) -> np.ndarray:
    """Extract one column as numpy array (still strings)"""
    return np.array([row[column] for row in data], dtype=str)


def extract_numeric_column(
    data: List[Dict[str, str]], column: str, missing_value: float = 0.0
) -> np.ndarray:
    """
    Extract numeric column, convert to float, replace missing values ('.', '', etc.)
    """
    values = []
    for row in data:
        val = row.get(column, "")
        if val in (".", "", "NA", "N/A"):
            values.append(missing_value)
        else:
            try:
                values.append(float(val))
            except ValueError:
                values.append(missing_value)
    return np.array(values, dtype=float)