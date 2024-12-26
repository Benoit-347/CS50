#we are currently using a general purpose data type in py like tuples, lists, dictionaries (more powerful)
#we can create our own data type called student using class
#classes are blueprints like for a house, here for pieces of data (house = object) or
# they are like a mould (classes) that you can define and give a name, using its blueprint you can create data types as you want
# they are used to define custom container with custom names

class Student:
    ...

a = int()
print(a)

variable1 = Student()   #assigning object type (like assigning int to a var)
variable1.name = input("Enter Name: ")  #here we are dynamically create attribute "name" (usually defined during class creation)
variable1.house = input("Enter House: ")        # which we can use to store specific values inside
print(variable1)
print(variable1.name, variable1.house)  #accessing attribures

#so its like acting (DO NOT ASSOCIATE AS EXACT) as a dict with keys as attribute and values as values specified