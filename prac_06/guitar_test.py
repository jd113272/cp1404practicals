from prac_06.guitar import Guitar

gibson_guitar = Guitar("Gibson L-5 CES", 1925, 16035.40)
another_guitar = Guitar("Another Guitar", 2015, 10000.50)
fifty_year_guitar = Guitar("50-year old guitar", 1975, 10000.50)
print(f"{gibson_guitar.name} get_age() - Expected 100. Got {gibson_guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")
print(f"{fifty_year_guitar.name} get_age() - Expected 50. Got {fifty_year_guitar.get_age()}")
print(f"{gibson_guitar.name} is_vintage() - Expected True. Got {gibson_guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
print(f"{fifty_year_guitar.name} is_vintage() - Expected True. Got {fifty_year_guitar.is_vintage()}")
