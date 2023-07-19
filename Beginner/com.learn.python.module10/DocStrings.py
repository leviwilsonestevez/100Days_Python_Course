def is_leap(year) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month) -> int:
    """This method check how much days have a particular month in one year. Check if a year is Leap or not """
    if 1 > month or month > 12:
        return 0
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

days_in_month()
year_inserted = int(input("Enter a year: "))
month_inserted = int(input("Enter a month: "))
days = days_in_month(year_inserted, month_inserted)
print(f"The number of days of the Month {month_inserted} in the year {year_inserted} is {days}")
