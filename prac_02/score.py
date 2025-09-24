"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Get score from user, generate random score and determine grades. """
    score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(grade)
    random_score = random.randint(0, 100)
    random_grade = determine_grade(random_score)
    print(random_grade)


def determine_grade(score: float):
    """Determine grade from given value."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
