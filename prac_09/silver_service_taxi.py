"""
Create a silver service taxi class which changes the fare based on fanciness.
"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Create an instance of the SilverServiceTaxi class."""
    flagfall = 4.5
    def __init__(self, fanciness, **kwargs):
        """Initialise an instance of the class."""
        self.fanciness = fanciness
        super().__init__(**kwargs)
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """Get the taxi fare, and add the flagfall amount."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string which includes the flagfall amount."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:,.2f}"