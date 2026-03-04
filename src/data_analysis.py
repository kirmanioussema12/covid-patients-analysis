import numpy as np
from typing import Dict, List, Tuple
from .data_cleaning import clean_regions_and_counts


def compute_daily_totals(
    dates: np.ndarray, values: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    """Sum values per unique date"""
    unique_dates, inverse_idx = np.unique(dates, return_inverse=True)
    daily_sums = np.bincount(inverse_idx, weights=values)
    return unique_dates, daily_sums


def top_n_days(
    dates: np.ndarray, values: np.ndarray, n: int = 5, ascending: bool = False
) -> List[Tuple[str, float]]:
    """Return top N days by value (descending by default)"""
    unique_dates, daily_sums = compute_daily_totals(dates, values)
    order = np.argsort(daily_sums)
    if not ascending:
        order = order[::-1]
    top_idx = order[:n]
    return list(zip(unique_dates[top_idx], daily_sums[top_idx]))


def seasonal_averages(dates: np.ndarray, values: np.ndarray) -> Dict[str, float]:
    """Very simple season grouping (Northern Hemisphere)"""
    month_to_season = {
        1: "Winter", 2: "Winter", 3: "Spring",
        4: "Spring", 5: "Spring", 6: "Summer",
        7: "Summer", 8: "Summer", 9: "Fall",
        10: "Fall", 11: "Fall", 12: "Winter",
    }

    season_values: Dict[str, List[float]] = {"Winter": [], "Spring": [], "Summer": [], "Fall": []}

    for date_str, val in zip(dates, values):
        try:
            month = int(date_str[5:7])
            season = month_to_season[month]
            season_values[season].append(val)
        except (ValueError, KeyError):
            continue

    averages = {}
    for season, vals in season_values.items():
        if vals:
            averages[season] = float(np.mean(vals))
    return averages


def group_by_region_stats(
    regions: np.ndarray, values: np.ndarray
) -> Dict[str, Dict[str, float]]:
    """Total and average per region"""
    unique_regions, _, inverse_idx = clean_regions_and_counts(regions)

    totals = np.bincount(inverse_idx, weights=values)
    counts = np.bincount(inverse_idx)
    averages = totals / np.where(counts > 0, counts, 1)  # avoid div/0

    result = {}
    for r, t, a in zip(unique_regions, totals, averages):
        result[r] = {"total": float(t), "average": float(a), "count": int(counts[unique_regions == r][0])}
    return result