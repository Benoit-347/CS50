# here we taken input, store a id and value, same as 1_.. but solved as a funtional/modular paradyme

# obtain string
def get_str_input(text):
    while True:
        returned = input(text)
        if returned.isalpha():
            return returned
        else:
            print("get_fn: input not aphabet")

# obtain 2D list, with nodes being (name, house) string.
def give_name_house(n):
    list1 = []
    for i in range(n):
        name = get_str_input("Enter Name:")
        house = get_str_input("Enter House: ")
        list1 = list1 + [[name, house]]
    return list1

# from a 2d list, with 2 elements in each node.
def print_all_pairs(list1):
    for i,j in list1:
        print(f"{i} is in {j} house")
        
def main():
    list_names_house = []
    number = int(input("enter number of inputs: "))
    list_names_house = list_names_house + give_name_house(number)
    print_all_pairs(list_names_house)

main()    