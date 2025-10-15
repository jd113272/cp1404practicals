"""
CP1404 practical
wimbledon exercise
Estimated time: 15 minutes
Actual time: 16 minutes
"""
filename = "wimbledon.csv"
CHAMPION_TO_COUNT = {}
winning_countries = set()
with open(filename, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()  # Ignore first line
    lines = in_file.readlines()

for line in lines:
    championship_data = line.split(",")
    country = championship_data[1]
    winning_countries.add(country)

    champion = championship_data[2]
    try:
        CHAMPION_TO_COUNT[champion] += 1
    except KeyError:
        CHAMPION_TO_COUNT[champion] = 1

print("Wimbledon champions: ")
for champion, number_of_wins in CHAMPION_TO_COUNT.items():
    print(f"{champion} {number_of_wins}")
number_of_countries = len(winning_countries)
print(f"These {number_of_countries} countries have won Wimbledon: ")
print(", ".join(sorted(winning_countries)))
