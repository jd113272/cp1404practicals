"""
Prompt user for 5 numbers and display information about these numbers, and confirm if user is authorised.
"""


def main():
    """Collect numbers from user and display information about the numbers. Also check if user is authorised"""
    numbers = []
    for i in range(0, 5):
        number = get_number()
        numbers.append(number)
    display_numerical_information(numbers)

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Please enter your name: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def display_numerical_information(numbers: list):
    """Print the numerical information based on user input."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[4]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def get_number():
    """Get a valid integer from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            integer = int(input("Number: "))
            is_valid_input = True
        except ValueError:
            print("Invalid number. Please try again.")
    return integer


main()
