total_cost = 0
number_items = int(input("Number of items: "))
if number_items < 0:
    while number_items < 0:
        print("Invalid number of items!")
        number_items = int(input("Number of items: "))
for i in range (0, number_items, 1):
    item_price = float(input("Price of item: "))
    total_cost = total_cost + item_price
if total_cost > 100:
    discount = total_cost * 0.1
    total_cost = total_cost - discount
print(f"Total price for {number_items} items is ${total_cost:.2f}")