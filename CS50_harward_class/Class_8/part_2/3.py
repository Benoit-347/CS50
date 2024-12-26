
class student:      
    ...

def put_object_variables(object, var1, var2):
     object.name = var1     #adds instance variable name specific to the object passed
     object.house = var2

def get_student():  
    name = input("Enter Name: ")
    house = input("Enter House: ")
    variable1 = student()    #called as construct call as it creates an object
    put_object_variables(variable1, name, house)    # did not use return as the attribute was not added only in local scope
    return variable1    #contains added attributes

def main():
      details = get_student()   #assigning the resultant object to a variable
      print(f"{details.name} is in {details.house} house")  #accessing the attributes of object

main()


