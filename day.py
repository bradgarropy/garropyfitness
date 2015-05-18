"""
day.py

Implements the day class.
"""


class Day(object):
    """Class which models a Day of measurements."""

    def __init__(self, date, weight, body_fat):
        self.date = date
        self.weight = weight
        self.body_fat = body_fat
