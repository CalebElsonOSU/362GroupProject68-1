def conv_num(num_str):
    """Converts a provided string to either an int or a float if possible,
    else returns None"""
    valid_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                  "7": 7, "8": 8, "9": 9}
    valid_hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                 "7": 7, "8": 8, "9": 9, "A": 10, "a": 10, "B": 11, "b": 11,
                 "C": 12, "c": 12, "D": 13, "d": 13, "E": 14, "e": 14,
                 "F": 15, "f": 15}
    decimal_count = 0
    negative = False
    ret = 0

    num_str, hexadecimal = check_if_hex(num_str)

    mult = 10 if not hexadecimal else 16

    # Empty string. Placed after hex check to catch empty hex strings
    if len(num_str) == 0:
        return None

    for index in range(len(num_str)):
        if num_str[index] == ".":
            decimal_count += 1
            mult = 0.1
            if decimal_count == 2 or hexadecimal:
                return None
        elif num_str[index] == "-":
            negative = True
            if index != 0:
                return None
        else:
            if (num_str[index] in valid_nums or
                    (num_str[index] in valid_hex and hexadecimal)):
                num = (valid_nums[num_str[index]] if not hexadecimal else
                       valid_hex[num_str[index]])
                # Move current ret left
                if decimal_count == 0:
                    ret = ret*mult + num
                # Move provided num and mult right
                else:
                    ret += num*mult
                    mult *= mult
            else:
                return None
    if negative:
        ret *= -1

    return ret


def check_if_hex(num_str):
    """"""
    hexadecimal = False

    # Hexadecimal found, change mult to 16 and remove leading 2 characters
    if len(num_str) >= 2 and (num_str[0:2] == "0x" or num_str[0:2] == "0X"):
        num_str = num_str[2:]
        hexadecimal = True

    return num_str, hexadecimal


def my_datetime(num_sec):
    """ Function finds the date by the seconds that have passed
     since 1-1-1970.
     """
    one_day = 86400
    month = 1
    year = 1970
    day = 1

    passed_days = num_sec // one_day
    if passed_days > 0:
        year_value = calculate_year(passed_days + 1, year)
        month_value = calculate_month(year_value[0], year_value[1], month)
        day = month_value[0]
        month = month_value[2]
        year = month_value[1]
    if day < 10:
        day = "0" + str(day)
    if month < 10:
        month = "0" + str(month)
    date = str(month) + "-" + str(day) + "-" + str(year)
    return date


def calculate_year(passed_days, year):
    """ Helper function finds the years that have passed and returns
    the found year and leftover days.
    """
    while passed_days > 366:
        if year % 4 != 0:
            passed_days = passed_days - 365
            year += 1
        else:
            if leap_year(year) is True:
                passed_days = passed_days - 366
                year += 1
            else:
                passed_days = passed_days - 365
                year += 1
    return passed_days, year


def calculate_month(passed_days, year, month):
    """ Helper function uses passed days to find the
    month and day of the date.
     """
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30_days = [4, 6, 9, 11]
    february = [2]
    while passed_days > 31:
        if month in months_with_31_days:
            passed_days = passed_days - 31
            month += 1
        elif month in months_with_30_days:
            passed_days = passed_days - 30
            month += 1
        elif month in february:
            check_if_leap_year = leap_year(year)
            if check_if_leap_year is True:
                passed_days = passed_days - 29
                month += 1
            else:
                passed_days = passed_days - 28
                month += 1
    if passed_days >= 28 and month == 2:
        check_if_leap_year = leap_year(year)
        if check_if_leap_year is False:
            passed_days = passed_days - 28
            month += 1
        elif passed_days == 30:
            passed_days = passed_days - 29
            month += 1
    if month == 13:
        month = 1
        year += 1
    return passed_days, year, month


def leap_year(year):
    """ Helper function calculates if the year was a leap year"""
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 100 == 0 and year % 400 == 0:
            return True
    else:
        return False
