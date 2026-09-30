# # Завдання 1
# # # def format_date(date_str):
# # #     parts = date_str.split("-")
# # #
# # #     year = parts[0]
# # #     month = parts[1]
# # #     day = parts[2]
# # #
# # #     new_date = day + "/" + month + "/" + year
# # #     return new_date
# # #
# # # print(format_date("2026-09-30"))  # Виведе: 30/09/2026
# Завдання 2
# from datetime import datetime, timedelta
#
#
# def next_monday(date_str):
#     date_obj = datetime.strptime(date_str, "%Y-%m-%d")
#     current_weekday = date_obj.weekday()
#     days_to_add = 7 - current_weekday
#
#     next_monday_obj = date_obj + timedelta(days=days_to_add)
#
#     return next_monday_obj.strftime("%Y-%m-%d")
#
# print(next_monday("2026-09-30"))
# Завдання 4
#
# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 != 0:
#         return True
#     else:
#         return False
#
# print(is_leap_year(2024))
# print(is_leap_year(2026))
