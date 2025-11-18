from sympy import *
t = symbols('t')
r = 4*(1+cos(t))
dr1 = diff(r, t)
dr2 = diff(dr1, t)
R = (r**2+dr1**2)**(3/2)/(r**2+2*dr1**2-r*dr2)
rho = R.subs(t, pi/2)
print("%0.3f"%(abs(rho)), "units")