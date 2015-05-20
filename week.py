"""
week.py

Implements the week class.
"""


class Week(object):
    """Class which models a Week of measurements."""

    def __init__(self, days):
        self.days = days
        self.weight_avg = 0
        self.body_fat_avg = 0
        self.weight_delta = 0
        self.body_fat_delta = 0

        # calculate weight average
        for day in days:
            self.weight_avg += day.weight

        self.weight_avg = self.weight_avg/len(days)

        # calculate body fat average
        for day in days:
            self.body_fat_avg += day.body_fat

        self.body_fat_avg = self.body_fat_avg/len(days)
