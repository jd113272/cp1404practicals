for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars):
    print("*", end='')
print()

# d.
number_of_lines = int(input("Number of lines: ")) + 1
for i in range (0, number_of_lines):
    for n in range (0, i):
        print("*", end='')
    print()
print()