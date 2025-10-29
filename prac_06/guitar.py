"""
Estimated time for guitar exercise: 45 minutes
Actual time: 46 minutes
"""
CURRENT_YEAR = 2025
VINTAGE_YEAR_THRESHOLD = 50


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar object.
        name = string
        year = int
        cost = float"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string output for guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Return the age of the guitar object."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return if the guitar object is vintage or not."""
        return True if self.get_age() >= VINTAGE_YEAR_THRESHOLD else False
