from pathlib import Path
from src.data_cleaning import clean_regions_and_counts

from src.data_loader import load_covid_data, extract_column, extract_numeric_column
from src.data_analysis import (
    compute_daily_totals,
    top_n_days,
    seasonal_averages,
    group_by_region_stats,
)
from src.utils import print_top_days, print_dict_with_title

DATA_PATH = Path("data/e760480e-1f95-4634-a923-98161cfb02fa.csv")


def main():
    print("Loading data...")
    data = load_covid_data(DATA_PATH)

    # ── Extract key columns ───────────────────────────────────────
    dates = extract_column(data, "date")
    regions = extract_column(data, "oh_region")
    hosp = extract_numeric_column(data, "hospitalizations")
    icu_covid = extract_numeric_column(data, "icu_current_covid")
    icu_vent = extract_numeric_column(data, "icu_current_covid_vented")

    # P2 ── Regions overview
    unique_regions, counts, _ = clean_regions_and_counts(regions)
    print("\nUnique OH regions:", list(unique_regions))
    print("Records per region:")
    for r, c in zip(unique_regions, counts):
        print(f"  {r:12} : {c:,d}")

    # P3 ── Hospitalizations
    total_hosp = hosp.sum()
    _, daily_hosp = compute_daily_totals(dates, hosp)
    avg_daily_hosp = daily_hosp.mean()
    print(f"\nTotal hospitalizations : {total_hosp:,.0f}")
    print(f"Average per day        : {avg_daily_hosp:,.1f}")

    # P4 ── Top 5 hospitalization days
    top_hosp_days = top_n_days(dates, hosp, n=5)
    print_top_days(top_hosp_days, "Top 5 days – Hospitalizations", "Hospitalizations")

    # P6 ── Seasonal pattern (hospitalizations)
    season_avg_hosp = seasonal_averages(dates, hosp)
    print_dict_with_title(season_avg_hosp, "Average hospitalizations by season")

    # P7 ── ICU analysis by region
    icu_region_stats = group_by_region_stats(regions, icu_covid)
    print("\nICU COVID stats by region:")
    for r, stats in icu_region_stats.items():
        print(f"{r:12}  total={stats['total']:>6.0f}   avg={stats['average']:>5.1f}")

    # P10 ── Top 5 ICU days
    top_icu_days = top_n_days(dates, icu_covid, n=5)
    print_top_days(top_icu_days, "Top 5 days – ICU COVID patients", "ICU COVID")


if __name__ == "__main__":
    main()