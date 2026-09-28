from datetime import date
def days_between_dates(date1_str, date2_str):
    d1 = date.fromisoformat(date1_str)
    d2 = date.fromisoformat(date2_str)
    return abs((d2 - d1).days)

days = days_between_dates("2026-01-01", "2026-01-15")
print(days)
