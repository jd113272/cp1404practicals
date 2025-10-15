"""
CP1404 prac 5
email exercise
Estimated time: 10 minutes
Actual time: 11 minutes
"""
EMAIL_TO_NAME = {}

email = input("Email: ")

while email != "":
    name = " ".join(email.split("@")[0].split(".")).title()
    confirmation = input(f"Is your name {name}? (Y/n) ")

    if confirmation.lower() != "y" and confirmation != "":
        name = input("Name: ")
    EMAIL_TO_NAME[email] = name

    email = input("Email: ")

for email, name in EMAIL_TO_NAME.items():
    print(f"{name} ({email})")
