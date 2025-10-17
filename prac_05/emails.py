"""
CP1404 prac 5
email exercise
Estimated time: 10 minutes
Actual time: 12 minutes
"""


def main():
    email_to_name = {}

    email = input("Email: ")

    while email != "":
        name = " ".join(email.split("@")[0].split(".")).title()
        confirmation = input(f"Is your name {name}? (Y/n) ")

        if confirmation.lower() != "y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name

        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
