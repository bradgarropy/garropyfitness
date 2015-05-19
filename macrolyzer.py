
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

