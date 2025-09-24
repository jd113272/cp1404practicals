"""
convert password to asterisks
"""
password = input("Please enter password: ")
minimum_length = 5

while len(password) < minimum_length:
    password = input("Please enter password: ")
print("*" * len(password))
