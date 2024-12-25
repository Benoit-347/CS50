
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



#what if we need to add a feature that if the name is padma, change house to Ravenclaw
def main3():
    student = get_student()
    if student[0] == "Harry":
        student[1] = " Gryffindor"
    print(f"{student[0]} is in {student[1]} house")

#we still use interations to get key names, how to go around that? use keys as column names instead of the data itself
#we want to use custom indexes i.e. keys (like we use index for lists)
# this is standard as key names shoud be unique and easy to asscess

def main6():
    student = get_student()
    if student["name"] == "Harry":
        student["house"] = "Gryffindor"
    print(f"{student['name']} is in {student['house']} house")

def get_student():
    name = input("Enter Name: ")
    house = input("Enter House: ")
    return {"name": name, "house": house}

main6()

def main_control(n_list):
    if 1 in n_list:
        main1()
    if 2 in n_list:
        main2()
    if 6 in n_list:
        main6()

main_control([6])
