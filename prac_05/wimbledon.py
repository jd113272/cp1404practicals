"""
CP1404 practical
wimbledon exercise
Estimated time: 15 minutes
Actual time: 40 minutes
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Output number of times each champion has won Wimbledon and which countries they represented."""
    lines = retrieve_file_data(FILENAME)
    champion_to_count, winning_countries = process_lines(lines)
    output_winning_countries(champion_to_count, winning_countries)


def process_lines(records):
    """Retrieve champions, the numbers of times each champion won and which countries have won Wimbledon."""
    champion_to_count = {}
    winning_countries = set()
    for record in records:
        country = record[COUNTRY_INDEX]
        winning_countries.add(country)
        champion = record[CHAMPION_INDEX]
        try:
            champion_to_count[champion] += 1
        except KeyError:
            champion_to_count[champion] = 1

    return champion_to_count, winning_countries


def output_winning_countries(champion_to_count, winning_countries):
    """Output winners, and their of wins, on new lines, as well as which countries have had winners."""
    print("Wimbledon champions: ")
    for champion, number_of_wins in champion_to_count.items():
        print(f"{champion}, {number_of_wins}")
    print(f"These {len(winning_countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(winning_countries)))


def retrieve_file_data(filename: str):
    """Return the CSV data as a list of lists for further processing."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Ignore first (header) line
        lines = [line.strip().split(",") for line in in_file.readlines()]
    return lines


main()
