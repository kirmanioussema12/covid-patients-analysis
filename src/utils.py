def print_top_days(results: list, title: str, value_name: str = "Value"):
    print(f"\n{title}\n")
    for date, val in results:
        print(f"{date:<20} | {value_name}: {val:>6.0f}")


def print_dict_with_title(d: dict, title: str):
    print(f"\n{title}\n")
    for k, v in d.items():
        print(f"{k:12} : {v:.2f}")