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
        self.fat_mass = None
        self.lean_body_mass = None

        # calulate only if weight and body fat have values
        if weight and body_fat:
            # calculate fat mass
            self.fat_mass = self.weight * (self.body_fat / 100)
            self.fat_mass = round(self.fat_mass, 1)

            # calculate lean body mass
            self.lean_body_mass = self.weight - self.fat_mass
            self.lean_body_mass = round(self.lean_body_mass, 1)
