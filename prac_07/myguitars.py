from guitar import Guitar


def main():
    lines = read_file()
    guitars = []
    add_guitars(guitars, lines)
    name = input("Please enter the name of your guitar: ")
    while name != "":
        get_guitar(guitars, name)
        name = input("Please enter the name of your guitar: ")
    print_guitar_list(guitars)
    update_file(guitars)


def add_guitars(guitars: list, lines: list[str]):
    for line in lines:
        # Format of file is: Name, Year, Cost. Format of class is: Name, Year, Cost.
        line = line.strip().split(",")
        instrument = Guitar(line[0], line[1], line[2])
        guitars.append(instrument)


def get_guitar(guitars, name):
    year = input("Please enter the manufacturing year: ")
    cost = input("Please enter the cost of your guitar: ")
    instrument = Guitar(name, year, cost)
    guitars.append(instrument)


def read_file() -> list[str]:
    with open('guitars.csv', 'r') as in_file:
        lines = in_file.readlines()
    return lines


def print_guitar_list(guitars):
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def update_file(guitars):
    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
