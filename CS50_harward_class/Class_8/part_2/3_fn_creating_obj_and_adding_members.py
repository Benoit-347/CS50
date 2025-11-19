# a fn to create members/ instances within a obj.
class student:      
    ...

# this fn called, by another fn that creates an obj then calls this fn to add members
def put_object_variables(object, var1, var2):    # adds instance variables, to the specific object, passed in arg.
     object.name = var1    
     object.house = var2

def get_student():  # creates a obj withing a fn, then adds members to the obj, then returns th obj
    name = input("Enter Name: ")
    house = input("Enter House: ")
    variable1 = student()    #called as construct call as it creates an object
    put_object_variables(variable1, name, house)    # did not use return as the attribute was not added only in local scope
    return variable1    #contains added attributes


def main():
      details = get_student()   # assigning the resultant object to a variable
      print(f"{details.name} is in {details.house} house")  #accessing the attributes of object

main()


