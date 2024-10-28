#is operator
#The is operator checks for object identity, not equality. 
# This means it compares whether the two operands are the same object in memory, not just whether their values are equal.
a= "123"
b = "str"
if type(a).__name__ is "str":
    print("yes")

elif b is "str":
    print("now yes")