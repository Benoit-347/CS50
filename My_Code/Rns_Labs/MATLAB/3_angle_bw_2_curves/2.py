from sympy import *
t = symbols('t')
r1 = sin(t) + cos(t)
r2 = 2*sin(t)
dr1 = diff(r1, t)
dr2 = diff(r2, t)
t1 = r1/dr1
t2 = r2/dr2
q = solve(r1-r2, t)
print("point of intersection is", q)
w1 = t1.subs({t:float(q[0])})
w2 = t2.subs({t:float(q[0])})
y1 = atan(w1)
y2 = atan(w2)
w = abs(y1-y2)
print("Angle between two polar curves in degrees is %0.2f"%(180*(w/pi)))