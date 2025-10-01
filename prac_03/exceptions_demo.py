"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
# 1. ValueError occurs when the input is anything other than an integer (e.g. floats and characters)
# 2. ZeroDivisionError occurs when the denominator input is 0.
# 3. To avoid the possibility of the ZeroDivisionError completely, a while loop can be used to get a denominator that is not equal to 0.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
