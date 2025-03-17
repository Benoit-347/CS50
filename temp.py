list_names = []
try:
    while True:                     #take input until EOF
        Input = input("Input: ")
        list_names.append(Input)
except EOFError:
    pass


def adieu(list_):
    length = len(list_)
    if length == 0:         # 4 conditions: Empty, 1 name, 2 names, 3 or more
        return 0
    elif length == 1:
        print(f"Adieu, adieu, to {list_[0]}")
    elif length ==2:
        print(f"Adieu, adieu, to {list_[0]} and {list_[1]}")
    else:
        print("Adieu, adieu, to ", end = "")
        for i in range(length-1):
            print(f"{list_[i]}, ", end = "")
        print(f"and {list_[length-1]}")
    return 0
adieu(list_names)
