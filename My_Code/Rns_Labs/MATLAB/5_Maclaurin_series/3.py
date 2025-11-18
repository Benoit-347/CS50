from sympy import *
x = symbols('x')
y = log(1 + cos(x))
dy = diff(y, x)
d2y = diff(dy, x)
d3y = diff(d2y, x)
d4y = diff(d3y, x)
y0 = y.subs(x, 0)
y1 = dy.subs(x, 0)
y2 = d2y.subs(x, 0)
y3 = d3y.subs(x, 0)
y4 = d4y.subs(x, 0)
y = y0 + x*y1 + x**2*y2/2 + x**3*y3/6 + x**4*y4/24
print("Maclaurin series is y =\n", y)