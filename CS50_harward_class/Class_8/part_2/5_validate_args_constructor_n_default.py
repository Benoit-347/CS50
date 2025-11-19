#how to validate the input data?
# we can validate withing the get_students fn itself, using raise keyword in py.
    # Chk if arg is None if None raise error. Returning None of fn alone will not help cause,
        # as there will exists an empty obj that may not be functoinal with rest of code relying of the members having data.

# can also make the __init__ fn to have default values to its parameters, so that passing the 3rd or nth argument is optional.
class Student:
    def __init__(self, name, house, color = None):
        if not (name and house):
            raise ValueError
        self.name = name
        self.house = house
        self.color = color

def get_student():
    name = input("Enter name: ")
    house = input("Enter house: ")
    flag_color = int(input("Choice- Want to input color? (1/0):"))
    color = None
    if flag_color == 1:
        color = input("Enter color: ")
    return Student(name, house, color)
    

def main():
    student = get_student()
    print(f"Name: {student.name} is in house: {student.house}", end = ' ')
    if student.color:
        print(f"with color: {student.color}")

main()