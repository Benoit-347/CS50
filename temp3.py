from sympy import *
r,t = symbols('x, y')
r = 4*(1+cos(t))
r1 = diff(r,t)
r2 = diff(r1,t)
rho = (r**2+r1**2)**1.5/(r**2+2*r1**2-r*r2)
rho1 = rho.subs(t, pi/2)
print('The radius of curvature is %0.3f units'% rho1)