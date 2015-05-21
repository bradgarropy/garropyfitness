"""
week.py

Implements the week class.
"""


class Week(object):
    """Class which models a Week of measurements."""

    def __init__(self, days):
        self.days = days

        # averages
        self.weight_avg = None
        self.lean_body_mass_avg = None
        self.fat_mass_avg = None
        self.body_fat_avg = None

        # deltas
        self.weight_delta = None
        self.lean_body_mass_delta = None
        self.fat_mass_delta = None
        self.body_fat_delta = None

        # calculate weight average
        for day in days:
            self.weight_avg += day.weight

        self.weight_avg = self.weight_avg/len(days)
        self.weight_avg = round(self.weight_avg, 1)

        # calculate body fat average
        for day in days:
            self.body_fat_avg += day.body_fat

        self.body_fat_avg = self.body_fat_avg/len(days)
        self.body_fat_avg = round(self.body_fat_avg, 1)

        # calculate fat mass average
        for day in days:
            self.fat_mass_avg += day.fat_mass

        self.fat_mass_avg = self.fat_mass_avg/len(days)
        self.fat_mass_avg = round(self.fat_mass_avg, 1)

        # calculate lean body mass average
        for day in days:
            self.lean_body_mass_avg += day.lean_body_mass

        self.lean_body_mass_avg = self.lean_body_mass_avg/len(days)
        self.lean_body_mass_avg = round(self.lean_body_mass_avg, 1)
