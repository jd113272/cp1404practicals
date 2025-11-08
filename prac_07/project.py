"""
CP1402 Project Management Program (Project Class).
"""


class Project:
    """Set up a Project object."""

    def __init__(self, name, start_date, priority, cost, completion_percentage):
        """Initialise Project object.
        name = string
        start_date = date
        priority = int
        cost = float
        completion_percentage = int"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string version of the object."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other, key):
        """Sort the objects by priority or by date."""
        if key == "priority":
            return self.priority < other.priority
        else:
            return self.start_date < other.start_date

    def is_complete(self):
        """Return if the project has been completed."""
        return self.completion_percentage == 100

    def export_project(self):
        """Return a string version of the object suitable for saving into a txt file."""
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost}\t{self.completion_percentage}"
