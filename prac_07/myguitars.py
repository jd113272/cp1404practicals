from guitar import Guitar

def main():
    lines = read_file()
    guitars = []
    add_guitars(guitars, lines)
    print_guitar_list(guitars)


def add_guitars(guitars: list, lines: list[str]):
    for line in lines:
        # Format of file is: Name, Year, Cost. Format of class is: Name, Year, Cost.
        line = line.strip().split(",")
        instrument = Guitar(line[0], line[1], line[2])
        guitars.append(instrument)


def read_file() -> list[str]:
    with open('guitars.csv', 'r') as in_file:
        lines = in_file.readlines()
    return lines

def print_guitar_list(guitars):
    guitars.sort()
    for guitar in guitars:
        print(guitar)

main()
