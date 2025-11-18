import sympy
x, y, z = sympy.symbols("x, y, z")
eqn1 = (x**2 + x**3)/(2*x)
eqn2 = (x**3 + 1)
eqn1 = sympy.simplify(eqn1)     # x*(x + 1)/2
print("1:",eqn1)

list1 = [[x, y, z], [x**2, y**2, z**2], [x**3, y**3, z**3]]
matrix = sympy.Matrix(list1)
Jac = sympy.simplify(sympy.det(matrix)) # calculates the total differentiation of the matrix
print(Jac)