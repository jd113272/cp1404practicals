"""
Test the unreliable car class.
"""
from unreliable_car import UnreliableCar


def main():
    """Test two instances of the UnreliableCar class."""
    # Test overridden init method.
    test_car = UnreliableCar("Car 1", 60, 32.8)
    assert test_car.reliability == 32.8

    second_test_car = UnreliableCar("Car 2", 80, 74.5)
    assert second_test_car.reliability == 74.5

    # Test overridden drive method.
    number_of_drives = test_drive_method(test_car)
    print(f"Of the 100 test runs, {number_of_drives} were driven. Expected drives: {round(test_car.reliability)}")
    number_of_drives = test_drive_method(second_test_car)
    print(
        f"Of the 100 test runs, {number_of_drives} were driven. Expected drives: {round(second_test_car.reliability)}")


def test_drive_method(car):
    """Test the drive method for a given instance."""
    number_of_completed_drives = 0
    for i in range(1, 100):
        distance_driven = car.drive(30)
        if distance_driven != 0:
            number_of_completed_drives += 1
            car.add_fuel(distance_driven)  # Replace fuel so car can keep driving.
    return number_of_completed_drives


main()
