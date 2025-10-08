"""
Generate the inputted number of lines of output, consisting of 6 random numbers between 1 and 45.
"""
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Output 6 random numbers between 1 and 45 on a single, for however many lines the user requests."""
    number_of_lines = get_number_of_lines()

    for i in range(0, number_of_lines):
        quick_pick = []
        create_unique_number(quick_pick)
        quick_pick.sort()
        line = [f"{number:2}" for number in quick_pick]
        print(" ".join(line))


def create_unique_number(quick_pick: list):
    """Generate a random number between 1 and 45 that is not already in the list."""
    for j in range(0, NUMBERS_PER_LINE):
        value = random.randint(MINIMUM, MAXIMUM)
        while value in quick_pick:
            value = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(value)


def get_number_of_lines() -> int:
    """Ask the user to input how many lines of quick picks they want."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number_of_lines = int(input("How many quick picks? "))
            if number_of_lines < 1:
                print("Invalid number. Quick picks must be greater than 0.")
            else:
                is_valid_input = True
        except ValueError:
            print("Error! Please enter a valid number")
    return number_of_lines


main()
