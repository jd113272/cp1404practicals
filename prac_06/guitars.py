"""
CP1404 Practical
Guitar program
"""
from prac_06.guitar import Guitar


def main():
    """Get a list of guitars from user and return a formatted output list."""

    print("My guitars!")
    guitars = get_new_guitars()

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("\n"
          "These are my guitars: ")
    print_guitar_list(guitars)


def print_guitar_list(guitars: list):
    """Print out a list of the user's guitars."""
    guitar_name_length = max([len(guitar.name) for guitar in guitars])
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>{guitar_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_new_guitars():
    """Return a list of guitars, based on user input."""
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: ").strip("$"))
        guitars.append(Guitar(name, year, cost))
        print(f"{guitars[-1]} added.")
        name = input("Name: ")
    return guitars


main()
