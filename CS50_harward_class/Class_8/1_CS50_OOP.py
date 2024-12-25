
def main1():
    name, house = get_student()
    print(f"{name} is in {house} house")

def get_student():
    name = input("Enter Name: ")
    house = input("Enter House: ")
    return name, house  #We can only return 1 data item as a whole

# here: 
# return name, house -> is taken as tuple i.e:
# return (name, house)

#using a tuple instead of py method

def main2():
    student = get_student()
    print(f"{student[0]} is in {student[1]} house")

def get_student():
    name = input("Enter Name: ")
    house = input("Enter House: ")
    return (name, house)  #We can only return 1 data item as a whole


#what if we need to add a feature that if the name is padma, change house to Ravenclaw
def main3():
    student = get_student()
    if student[0] == "Harry":
        student[1] = " Gryffindor"
    print(f"{student[0]} is in {student[1]} house")

def get_student():
    name = input("Enter Name: ")
    house = input("Enter House: ")
    return (name, house)


def main_control(n_list):
    if 1 in n_list:
        main1()
    if 2 in n_list:
        main2()

main_control([1,2])



