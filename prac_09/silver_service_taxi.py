"""

"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """"""
    flagfall = 4.5
    def __init__(self, fanciness, **kwargs):
        """"""
        self.fanciness = fanciness
        super().__init__(**kwargs)
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:,.2f}"