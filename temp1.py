from sympy import *
x, y = symbols('x, y')
a= 3
y = 2*sqrt(a*x)
y1 = diff(y,x)
y2 = diff(y1,x)
rho = (1+y1**2)*(1.5)/y2
rho1 = rho.subs(x,a)
print('The radius of curvature is %0.3f units'% abs(rho1))