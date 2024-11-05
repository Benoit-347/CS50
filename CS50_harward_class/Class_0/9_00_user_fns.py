#write our own functions?
#use def statement

#syn:
#def <fn_name>():
#    <tasks>

def a():
    print("hello")


#in Python, function declarations are processed when the code is executed
#when the code is executed, but the function's body code is not executed until the function is called

# When Py interpreter reaches a def statement, it creates a function object and assigns it to the function's name, making it available for later use.


#can do operations by using parameters (para -> var representing input during fn declaration)
def hello(b):   #here b is a parameter
    print(f"hello {b}")

hello("benoit") #here "benoit" is a argument
#note: the var b is defined only in local scope


#how to store value after function doing work?
#1 return, 2 global
def get_num():
    n = int(input("enter number:"))
    return n #temporaryly gives the value (next to return) when fn call is used (when assigned or taken as input for another fn/operator)
print(get_num())

#abstraction: potraying a idea(potentially complex) into language