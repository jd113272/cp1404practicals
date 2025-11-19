"""
Create an unreliable car class that inherits from Car, but considers reliability.
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Represent an instance of an unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an instance of the unreliable car class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a random distance if it is less than the car's reliability."""
        random_distance = random.randint(0, 100)
        if random_distance < self.reliability:
            distance_driven = random_distance
        else:
            distance_driven = 0
        return distance_driven
