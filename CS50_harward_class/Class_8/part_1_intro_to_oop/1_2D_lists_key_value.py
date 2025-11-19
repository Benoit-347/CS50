#procedural way to solve problems
# get name and house, n times. Store them into list of (name, houes). Later print them, each node.
# Q) To take name and house of a person
list1 = []
for i in range(int(input("enter num of inputs: "))):
    while True:
        name = input("enter name: ")
        if type(name).__name__ == "str":
            break
    while True:
        house = input("enter house: ")
        if type(name).__name__ == "str":
            break
    list1 = list1 + [[name, house]]
print(list1)
for i, j in list1:
    print(f"{i} is in {j}")


