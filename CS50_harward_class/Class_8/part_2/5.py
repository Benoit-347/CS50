#how to validate the input data?
# we can validate withing the get_students fn itself, but now you can use classes
# like how we like taking common terms in braces in math, classes by itself allowes you to encapsulate the object such that it meets your req
# timestamp - 54:58
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def get_student():
    name = "benoit"
    house = "Red"
    return Student(name, house)
    

def main():
    student = get_student()
    print(f"{student.name} is in {student.house} house")

main()