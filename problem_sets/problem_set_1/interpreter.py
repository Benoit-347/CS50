operation = input("Expression: ")
x, Y, z = operation.split()     #obtain terms seperated by space
X = int(x)
Z = int(z)
def print_1_dec(a):         #to get 1 decimal place
    print(f"{a:.1f}")

def operate(X, Y, Z):
    if Y == "+":
        return X+Z
    elif Y == "-":
        return X-Z
    elif Y == "*":
        return X*Z
    elif Y == "/":
        return X/Z

print_1_dec(operate(X,Y,Z))     #calling fns
