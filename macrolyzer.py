
"""
macrolyzer.py

Module that tracks weight trends over time.
"""


import day
import week
import datetime
import myfitnesspal


def main():
    """Retrieves and analyzes weight and body fat from MyFitnessPal."""

    # retrieve and parse command line arguments
    args = parse_args()

    # create MyFitnessPal client
    client = myfitnesspal.Client(args.username, args.password)

    # establish a 5 week date range
    start_date = datetime.date.today()
    end_date = start_date - datetime.timedelta(weeks=5)

    # retrieve weight and body fat measurements
    weight = client.get_measurements('Weight', start_date, end_date)
    body_fat = client.get_measurements('Body Fat', start_date, end_date)

    # create list of day objects for every date in the range
    days = create_days(start_date, end_date, weight, body_fat)

    # create week objects from the day objects
    weeks = create_weeks(days)



    # TODO: Calculate week changes

    # TODO: Print to HTML


def parse_args():
    """Defines command line argument structure and returns arguments."""

    import argparse

    parser = argparse.ArgumentParser()

    # define arguments
    parser.add_argument("username", help="MyFitnessPal username")
    parser.add_argument("password", help="MyFitnessPal password")
    
    args = parser.parse_args()

    return args


def create_days(start_date, end_date, weight, body_fat):
    """Create day objects from measurements."""

    current_date = start_date
    step = datetime.timedelta(days=1)

    date_range = []

    # create a list of dates within the range
    while current_date >= end_date:
        date_range.append(current_date)
        current_date -= step

    days = []

    # loop over each day in the range
    for date in date_range:
        # retrieve the values for the current day object
        current_date = date
        current_weight = weight.get(current_date, None)
        current_body_fat = body_fat.get(current_date, None)

        # create the day object
        current_day = day.Day(current_date, current_weight, current_body_fat)

        # add the current day to the list of days
        days.append(current_day)

    return days


def create_weeks(days):
    """Create week objects from measurements."""

    weeks = []

    # loop over each week in the range
    for index in range(0, len(days), 7):

        # create a slice of seven days
        days_list = days[index:index + 7]

        # create the week object
        current_week = week.Week(days_list)

        # add the current week to the list of weeks
        weeks.append(current_week)

    return weeks

if __name__ == "__main__":
    main()
