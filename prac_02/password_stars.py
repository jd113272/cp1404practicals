"""Convert password to asterisks."""


def main():
    """Convert a given password to asterisks."""
    minimum_length = 5
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password: str):
    """Print a specific number of asterisks."""
    print("*" * len(password))


def get_password(minimum_length: int) -> str:
    """Get a valid password from user."""
    password = input("Please enter password: ")

    while len(password) < minimum_length:
        password = input("Please enter password: ")
    return password


main()
