item_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def return_total(item, total):      # used to add item value to total and print total
    if item in item_dict:
        total += item_dict[item]
        print(f"Total: ${total:.2f}")
    return total

total = 0
while True:
    try:
        item = input("Item: ").lower().title()
        total = return_total(item, total)

        if item == "^D":    # vs code sometimes takes the input of ctrl D as ^D
            break

    except EOFError:
        break
