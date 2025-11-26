"""
Test the Silver Service Taxi class.
"""
from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi(fanciness=4, name="Hummer", fuel=200)
assert hummer.flagfall == 4.5
assert hummer.fanciness == 4
assert hummer.price_per_km == 4.92
assert str(hummer) == "Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50"
print(hummer)

silver_taxi = SilverServiceTaxi(fanciness=2, name="Second silver taxi", fuel=200)
assert silver_taxi.flagfall == 4.5
assert silver_taxi.fanciness == 2
assert silver_taxi.price_per_km == 2.46
assert str(silver_taxi) == "Second silver taxi, fuel=200, odo=0, 0km on current fare, $2.46/km plus flagfall of $4.50"
silver_taxi.drive(18)
assert str(silver_taxi) == "Second silver taxi, fuel=182, odo=18, 18km on current fare, $2.46/km plus flagfall of $4.50"
print(silver_taxi)
assert silver_taxi.current_fare_distance == 18
assert silver_taxi.get_fare() == 48.8
