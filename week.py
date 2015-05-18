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
