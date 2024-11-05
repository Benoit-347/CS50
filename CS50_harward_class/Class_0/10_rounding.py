#using built in fns to round off float values

def main():
    global a
    a = float(5.5)
    to_int()
    using_round()
    using_special_print()
    usingmath()

#converts float to int by removing decimal
def to_int():
    b = int(a)
    print(f"int():                  {b}")

#round off the decimal until specified secimal space
def using_round():
    #using round fn
    print(f"round(a):               {round(a)}")
    x = 2.22325
    y  = round(x,4)
    # (default val is 0 and converts to int), number next shows upto how many decimal places
    print(f"round(2.22325, 4):      {y}")

def using_special_print():
    x =99999.88888
    print(f"x:,                     {x:,}")
    #for the variable in flower brackets, show comma after every 3 digits in the printed message
    print(f"x:.2f                   {x:.2f}")
    #in format string in flower brackets colon then .n denotes number of digits roundoff to, does same as function below:
    print(f"round(99999.88888):     {round(x,2)}")

def usingmath():
    #lowest integer not less than a and highest integer not more than a
    import math       
    lower_int = math.floor(a)  # Results in 3
    higher_int = math.ceil(a)
    print(f"5.5 math module floor,ceil: {lower_int, higher_int}")


main()