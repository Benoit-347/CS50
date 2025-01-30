import sympy
x, y = sympy.symbols('x y')
A = x*(x + 1)
B = x + x**2
if A == B:
    print("Yes")
else:
    print("No")
print(A, B)