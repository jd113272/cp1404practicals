"""
Simulate taxi trips.
"""
from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit c)hoose taxi d)rive\n>>> "


def main():
    """Get the user to select/drive a taxi, and add to the fair until 'q' is pressed."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    trip_cost = 0.0
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            charge = drive_taxi(current_taxi, taxis)
            trip_cost += charge
        else:
            print("Invalid option")
        print(f"Bill to date: ${trip_cost:,.2f}")
        choice = input(MENU).lower()
    print(f"Total trip cost: ${trip_cost:,.2f}\n"
          f"Taxis are now:")
    print_available_taxis(taxis)


def choose_taxi(taxis):
    """Get the user to select a taxi from the list of taxis."""
    print("Taxis available:")
    print_available_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    if taxi_choice > (len(taxis) - 1):
        print("Invalid taxi choice")
        taxi_choice = None
    return taxi_choice


def print_available_taxis(taxis):
    """Print the list of available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(taxi_number, taxis):
    """Drive the taxi the distance desired by the user."""
    if taxi_number is not None:
        distance = int(input("Drive how far? "))
        current_taxi = taxis[taxi_number]
        current_taxi.start_fare()
        current_taxi.drive(distance)
        charge = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip will cost you ${charge:.2f}")
    else:
        print("You need to choose a taxi before you can drive")
        charge = 0
    return charge


main()
