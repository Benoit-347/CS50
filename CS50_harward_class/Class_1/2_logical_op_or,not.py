#logical operators: or, and, not #they are keywords
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:      #True or False == True, False or False == False
    print("x is not equal to y")
else:
    print("x is equal to y")
