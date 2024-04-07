# Assignment: DEV108 Review 1: Seasons Detector
# Class: DEV 128
# Date 4/4/2024
# Author: Rob Ranf
# Description: Program to determine the season given the month and date.

import datetime


# The get_month() function gets the month as an int from user input and validate it.
def get_month() -> int:
    input_month = int(input("Please enter the month (between 1 and 12): "))
    while input_month < 1 or input_month > 12:
        print("Invalid month entered")
        input_month = int(input("Please enter the month (between 1 and 12): "))
    return input_month


# The get_day() function gets the day of the month as
# an int from user input and validates it.
def get_day(month: int) -> int:
    day_check = check_input_month(month)
    input_day = int(input(day_check))
    while input_day < 1 or input_day > 31:
        print("Invalid day entered")
        input_day = int(input(day_check))
    return input_day


# The check_input_month() function checks the month and prompts
# the user for a day based on the month entered.
def check_input_month(month: int) -> str:
    if month in (1, 3, 5, 7, 8, 10, 12):
        return "Please enter the day (between 1 and 31): "
    elif month == 2:
        return "Please enter the day (between 1 and 28): "
    else:
        return "Please enter the day (between 1 and 30): "


# The get_day_of_year() function gets the day number of the year using the datetime
# module's timetuple() method and the timetuple()'s tm_yday property.
def get_day_of_year(month: int, day: int) -> int:
    formatted_month_day = "%Y-%m-%d"
    # Use 2023 to account for that we're assuming it's not leap year and have
    # the datetime module calculate day of the year based on this.
    month_day = "2023" + "-" + str(month) + "-" + str(day)
    # The datetime module expects a time value to be passed when formatting is used.
    # Because one isn't needed, the time value is null in our formatted month and day,
    # however the strptime() method must still be called to remove the empty time value.
    # (I think there's likely an easier way to do this, however I have only ever passed
    # a formatted date/time string into datetime)
    result = datetime.datetime.strptime(month_day, formatted_month_day)
    day_year_tuple = result.timetuple()
    day_year = day_year_tuple.tm_yday
    return day_year


# The get_season() function determines the season based on the day of the year.
# Day of the year calendar: https://www.esrl.noaa.gov/gmd/grad/neubrew/Calendar.jsp
def get_season(day_of_year: int) -> str:
    if 1 <= day_of_year <= 74:
        return "Winter"
    elif 75 <= day_of_year <= 166:
        return "Spring"
    elif 167 <= day_of_year <= 258:
        return "Summer"
    elif 259 <= day_of_year <= 349:
        return "Fall"
    else:
        return "Winter"


# The main() function is the program entrypoint.
def main():
    again = "y"
    while again == "y":
        print("Welcome to the Seasons program")
        month = get_month()
        day = get_day(month)

        try:
            day_of_year = get_day_of_year(month, day)
        except ValueError:
            print("Please enter a day that corresponds to the correct number of days in "
                  "this month.")
            month = get_month()
            day = get_day(month)
            day_of_year = get_day_of_year(month, day)

        season = get_season(day_of_year)
        print(f"Season = {season}")
        again = input("Enter another input? (y/n): ").lower()
    print("Goodbye!")


if __name__ == "__main__":
    main()
else:
    main()
