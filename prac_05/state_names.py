"""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
MAXIMUM_CODE_LENGTH = 3  # key is not expected to be longer than 3 characters.

for abbreviation, state_name in CODE_TO_NAME.items():
    print(f"{abbreviation:{MAXIMUM_CODE_LENGTH}} is {state_name}")
state_code = input("Enter short state: ").upper()

while state_code != "":
    try:
        print(f"{state_code:{MAXIMUM_CODE_LENGTH}} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
