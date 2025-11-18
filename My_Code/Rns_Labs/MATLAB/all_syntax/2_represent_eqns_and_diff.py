import sympy
x, y = sympy.symbols("x,y")   # denote the symbolic form of "x" to var x (can use space instead of ,)
eqn1 = x**2 + y + 5
eqn2 = x**2 -y + 2
# assume the eqns are equal, when they are differentiated wrt x to find soln

diff_1 = sympy.diff(eqn1, x)    # = 2x
diff_2 = sympy.diff(eqn2, x)    # = 2x

ans = sympy.solve([diff_1, diff_2], x)  # pass eqns in arg 1, gives list for non list type (1 eqn) and dict for multiple eqn
x_ans = ans[x]

result  = diff_1.subs({x: x_ans}) #subbing a eqn to a eqn: subs([(x, 5), (y, x + 1)])
print(result)

# abs(), atan()