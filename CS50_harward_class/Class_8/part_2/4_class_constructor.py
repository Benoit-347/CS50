# a constructor is a feature of a class, where at obj initialization, arguments can be passed within class parameters
                                            # the arguments will be assigned to the obj's member.


#1. __init__ during construction call, used to create members/attributes by simply passing arguments to class.


# its a feature of java as well, where a method is created withing a class, whose name is same as class name and the parameters of the method denote the parameters taken duting class call, and the same method body denotes how and which member is assigned and what work is pre-done during constructor call.


# __init__ the first arg is passed automatically by pyVM, the reference of the current object. 
class student:      
    def __init__(___, name, house):    #__init__ is a py term used to call this fn each time the class is used to construct (obj creation i.e. in construct call) and it performs the whole fn body.
        ___.name = name
        ___.house = house
        print("Assigned members; gg")
    # the self parameter is syn for passing the doing actions to the object to be used on
    # serves as a placeholder for the actual object

# we use __init__ as we want to create attributes each time an object is created,
    # unlike assigning attributes after the object is constructed

def get_student():  
    name = input("Enter Name: ")
    house = input("Enter House: ")

    # construct call:
    variable1 = student(name, house)    #passing arguments for object (called attribute / instace variable)
    return variable1                    #this is treated as a function
    # obsrve: the arguments next to class name is passed to __init__ fn 
        # which then uses the arguments on "self" syntaically meaning a reference to the object that was just created
 

def main():
      details = get_student()
      print(f"{details.name} is in {details.house} house")

main()

# note: automatically (not req) __new__ used to handle creating an empty object in memory for us