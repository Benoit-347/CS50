dict_items = {}
while True:
    try:
        item = input().upper()
        if item == "^D":        # vs code sometimes takes the input of ctrl D as ^D
            break
        elif item in dict_items:
            dict_items[item] += 1
        else:
            dict_items.setdefault(item, 1)  # adds item as key to dict if not exist, with value 1

    except EOFError:
        break

for i in sorted(dict_items):
    print(f"{dict_items[i]} {i}")
