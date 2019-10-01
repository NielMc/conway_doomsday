def calculate_leap_year(year):
    """
    Returns a boolean for whether the given year is
    a leap year or not
    """

    return True if year % 4 == 0 and year % 400 > 0 else False

def calculate_century_key(year):
    """
    Returns an integer for the doomsday calculation based
    on the current century
    """

    keys = {0: 2,
            100: 0,
            200: 5,
            300: 3}

    century = year - (year % 100)

    return keys[century % 400]

def calculate_doomsday(year):
    """
    Returns the doomsday for a given year using Conway's
    algorithm
    """

    century_key = calculate_century_key(year)
    first_year_part = int((year % 100) / 12)
    second_year_part = int(year % 100) % 12
    divided_figure = int(second_year_part / 4)

    return (century_key + first_year_part + second_year_part + divided_figure) % 7

def calculate_day_of_week(day, month, year):
    """
    Checks the tables and calculates the day of the week
    based on Conway's doomsdays
    """

    doomsday_table = {3: 7,
                      4: 4,
                      5: 2,
                      6: 6,
                      7: 4,
                      8: 1,
                      9: 5,
                      10: 3,
                      11: 7,
                      12: 5}

    day_of_week_table = {0: "Sunday",
                         1: "Monday",
                         2: "Tuesday",
                         3: "Wednesday",
                         4: "Thursday",
                         5: "Friday",
                         6: "Saturday"}

    doomsday = calculate_doomsday(year)
    leap_year = calculate_leap_year(year)
    print(doomsday)

    if month == 1:
        doomsday_to_check = 4 if leap_year else 3
    elif month == 2:
        doomsday_to_check = 1 if leap_year else 7
    else:
        doomsday_to_check = doomsday_table[month]

    if day == doomsday_to_check:
        weekday = doomsday
    elif day > doomsday_to_check:
        weekday = doomsday + ((day - doomsday_to_check) % 7)
    else:
        weekday = (doomsday - doomsday_to_check) + day

    return day_of_week_table[weekday % 7]

if __name__ == "__main__":
    input_day = int(input("Input the date - day: "))
    input_month = int(input("Input the date - month: "))
    input_year = int(input("Input the date - year: "))

    print(calculate_day_of_week(input_day, input_month, input_year))
