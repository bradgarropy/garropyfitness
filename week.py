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
        avg_list = [day.weight for day in days if day.weight]
        self.weight_avg = average(avg_list)

        # calculate lean body mass average
        avg_list = [day.lean_body_mass for day in days if day.lean_body_mass]
        self.lean_body_mass_avg = average(avg_list)

        # calculate fat mass average
        avg_list = [day.fat_mass for day in days if day.fat_mass]
        self.fat_mass_avg = average(avg_list)
        
        # calculate body fat average
        avg_list = [day.body_fat for day in days if day.body_fat]
        self.body_fat_avg = average(avg_list)


def average(avg_list):
    avg = sum(avg_list) / len(avg_list)
    avg = round(avg, 1)

    return avg
