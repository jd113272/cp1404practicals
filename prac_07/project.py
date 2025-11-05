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
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"