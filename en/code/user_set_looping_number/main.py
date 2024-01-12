shopping = []

how_many = input("How many items of shopping do you have? ")
how_many = int(how_many)

for item_number in range(how_many):
    item = input(f"What is item number {item_number}? ")
    shopping.append(item)

print(shopping)