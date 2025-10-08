"""
Generate the inputted number of lines of output, consisting of 6 random numbers between 1 and 45.
"""
import random
is_valid_input = False
while not is_valid_input:
    try:
        number_of_lines = int(input("How many quick picks? "))
        is_valid_input = True
    except ValueError:
        print("Error! Please enter a valid number")


for i in range(0, number_of_lines):
    numbers = []
    for j in range(0, 6):
        value = random.randint(1, 45)
        while value in numbers:
            value = random.randint(1, 45)
        numbers.append(value)
    numbers.sort()
    line = [str(number) for number in numbers]
    print(" ".join(line))