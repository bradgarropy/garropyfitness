
"""
macrolyzer.py

Module that tracks weight trends over time.
"""


import day
import datetime
import myfitnesspal

# create MyFitnessPal client
client = myfitnesspal.Client('username','password')

# establish a 5 week date range
today = datetime.date.today()
past = today - datetime.timedelta(weeks=5)

# retrieve weight and body fat measurements
weight = client.get_measurements('Weight', today, past)
body_fat = client.get_measurements('Body Fat', today, past)

# calculate the date range
date_range = (today - past).days

days = []

# loop over each day in the range
for delta in range(0, date_range + 1):

    # retrieve the values for the current day object
    current_date = today - datetime.timedelta(days=delta)
    current_weight = weight[current_date]
    current_body_fat = body_fat[current_date]

    # create the day object
    current_day = day.Day(current_date, current_weight, current_body_fat)

    # add the current day to the list of days
    days.append(current_day)

