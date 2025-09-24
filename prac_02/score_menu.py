"""Create an interactive score based menu."""

# CONSTANTS
MENU = ("G: Get valid score (0-100) \n"
        "P: Print result \n"
        "S: Show stars \n"
        "Q: Quit")


def main():
    """Create an interactive menu."""
    score = get_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            result = determine_grade(score)
            print(result)
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid Input")
        print(MENU)
        choice = input(">>> ").upper()
    print("farewell")


def get_score():
    """Get a number from user between 0 and 100 (inclusive)."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid integer.")
        score = int(input("Enter score: "))
    return score


def determine_grade(score: float):
    """Determine grade level of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
