#operators
# + - * / ** // %
def add(a, b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def exponent(a,b):
    return a**b
def floor_division(a,b):
    return a//b     #note floor division of a negative number returns whole number that tends to -ve infinity (assume it divides until remainder is +ve)
def modulus(a,b):
    return a%b      #note floor division of a negative number returns + ve whole number that is given by above (assume it divides until remainder is +ve)
print(f"1. {add(11, 3)}\n2. {subtract(11,3)}\n3. {multiply(11,3)}\n4. {divide(11,3)}\n5. {exponent(11,3)}\n6. {floor_division(11,3)}\n7. {modulus(11,3)}")