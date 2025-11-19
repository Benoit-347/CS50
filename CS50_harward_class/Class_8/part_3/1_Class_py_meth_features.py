# You can customize a class, for its obj to return a string, in case the obj itself is printed
    # u have to create a fn with fn_name '__str__' within that class.
        # __str__ can only print a string and no other data type.

class Student:
    ...

    def __init__(self, name, house):
        print("Created obj")
        self.name = name
        self.house = house
        print("Assigned obj")


    def __str__(self):
        return f"I am a of <class 'Student'>\nI got attributes:\nname: {self.name}\nhouse: {self.house}"     # f"I am a of <class 'Student'> <obj '{self}'" -> putting self here would cause an infinite call on obj which would return a string containing the obj, a infite recursive call.

def main():
    obj = Student("Benoit", "House")
    print(obj)

main()