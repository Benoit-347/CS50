# instance (object) methods
#python's feature of using classes


#1. __init__ used to create attributes by simply passing arguments right during construction call


#in java there are fns explicitly called constructors that construct object and initialize values
# in python we call the __init__ the initialization method


class student:      
    def __init__(self, name, house):    #__init__ is a py term used to call this fn each time the class is used in construct call, to perform the below statement
        self.name = name
        self.house = house
    # the self parameter is syn for passing the doing actions to the object to be used on
    # serves as a placeholder for the actual object

# we use __init__ as we want to create attributes each time an object is created,
# unlike creating objects dynamically after the object is constructed

def get_student():  
    name = input("Enter Name: ")
    house = input("Enter House: ")

    # construct call:
    variable1 = student(name, house)    #passing arguments for object (called attribute / instace variable)
    return variable1                    #this is treated as a function
    #the arguments next to class name is passed to __init__ fn 
    # which then uses the arguments on "self" syntaically meaning a reference to the object that was just created
 
def main():
      details = get_student()
      print(f"{details.name} is in {details.house} house")

main()

#in world its like using a blueprint for houses with only thing varying is the name of house and paint
# llly here blueprint of object.name and .house are structures that take in values when passed into as arguments

# note: automatically (not req) __new__ used to handle creating an empty object in memory for us