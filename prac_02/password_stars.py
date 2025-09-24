"""convert password to asterisks"""


def main():
    minimum_length = 5
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password: str):
    print("*" * len(password))


def get_password(minimum_length: int) -> str:
    password = input("Please enter password: ")

    while len(password) < minimum_length:
        password = input("Please enter password: ")
    return password


main()
