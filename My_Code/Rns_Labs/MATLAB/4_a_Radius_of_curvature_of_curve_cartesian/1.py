from sympy import *
x = symbols('x')
a = 3
y = 2*sqrt(a*x)
dy1 = diff(y, x)
dy2 = diff(dy1, x)
r = (1+dy1**2)**(3/2)/dy2
R = r.subs({x:3})
print("ROC_P:%0.3f"%abs(R), "units")