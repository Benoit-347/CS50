import sympy
x, y, z = sympy.symbols("x, y, z")
f1 = (12 - y - z) / 10
f2 = (12 - x - z) / 10
f3 = (12 - x - y) / 10
"""
Lambdify:
It is- SymPy converts symbolic expressions or matrices into callable numerical functions. It also allows fast evaluation with numerical inputs instead of symbolic manipulation.
Takes three main arguments:
    Symbols: The variables (e.g., x) in the expression.
    Expression: The SymPy object (e.g., x**2 + 3, a Matrix).
    Module: The backend (e.g., 'numpy', 'math') for numerical evaluation.
"""
g1 = sympy.lambdify([x, y, z], f1)
g2 = sympy.lambdify([x, y, z], f2)
g3 = sympy.lambdify([x, y, z], f3)
x0, y0, z0 = 0, 0, 0
i = 1
while i<= 5:
    x1 = g1(x0, y0, z0)
    y1 = g2(x1, y0, z0)
    z1 = g3(x1, y1, z0)
    
    print('%d\t %0.4f\t%0.4f\t%0.4f\n' %(i, x1, y1, z1))
    i += i
    x0 = x1
    y0 = y1
    z0 = z1

print("\nSolution: x = %0.3f, y = %0.3f and z = %0.3f\n" %(x1, y1, z1))