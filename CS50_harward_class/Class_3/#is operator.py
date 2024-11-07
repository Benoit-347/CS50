#is operator
#The is operator checks for object identity, not equality. 
# This means it compares whether the two operands are the same object in memory, not just whether their values are equal.

a= "123"
b = "str"
if type(a).__name__ is "str":
    print("yes")

elif b is "str":
    print("now yes")

c = b
if c is b:
    print("2a. yes")

#for the below code onwards:
#The code might be printing "2b. yes" instead of "2b. No" due to Python's internal string interning, which can make small, frequently used strings (like "str") point to the same memory address.

#Explanation of Python String Interning
#In Python, certain strings are interned to optimize memory usage and performance, especially short strings or strings that look like identifiers (e.g., variable names). When a string is interned, identical string literals will point to the same memory location, even if they're created separately.


c = "str"
if c is b:
    print("2b. yes")
else:
    print("2b. No")

b = "1234fewf"
c = "1234fewf"
if c is b:
    print("3b. yes")
else:
    print("3b. No")

a = "123"
b = "different_string"
c = b
c = "different_string"
if c is b:
    print("4b. yes")
else:
    print("4b. No")

#Python's string interning mechanism is an optimization that makes certain strings (especially short, frequently reused ones like "str") refer to the same memory location. This behavior can vary slightly between environments and implementations, but it’s common for short strings and identifiers.