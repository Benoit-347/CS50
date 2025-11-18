import sympy

#symbols()
"""designed for symbolic computation, enabling algebraic manipulations, calculus, and equation solving.
# normally when we differentiate we need to do so as a var not numeric
 It is used in mathematical research and engineering for handling mathematical expressions symbolically rather than numerically."""
sympy.symbols('x')  #used to define symbolic variables that can represent mathematical symbols in expressions.
x, y= sympy.symbols('x y') #syn: symbols(names, **kwargs)  names = "x y"   kwargs: positive = True, integer = True, real = True
                        #sympy.symbols('<var_name_1> <var_name_2>')
z = x**2
print(1, z)

#kwargs use case
y = sympy.symbols('x', positive = True)
print(2, y<0)


#expand()   #expands the values in curly braces
result1 = (x+ y)**2
result2 = sympy.expand((x+ y)**2)
print(3, result1)
print(4, result2)

y = sympy.symbols('y', positive = True)
result2 = sympy.expand((x+ y)**2)
result1 = (x+ y)**2


#diff(f, x) #differentiates 1st parameter wrt 2nd
print(5, sympy.diff(result2, x))
print(6, sympy.diff(result1, x))    #note here that it even diff when not expanded
print(7, sympy.diff(result1, x, 2, y, 2))   #syn: diff(fn, <var_name>, <(optional) degree>, <(optional) var_name_2>, <(optional) degree>)
#want to keep differed fn as (fn)'? 
# in diff fn use keyword "evaluate" = False 
print(6.2, sympy.diff(result1, x, evaluate = False))


#to find values of variables that satisfies a particular equation?
#solve()    
print(8, sympy.solve(x**2, x)) #syn: solve(<fn>, <for_var>) 
# default = the symbols used in 1st para
fn1 = x**2 - 4 + y
fn2 =  y-x-1
print(8.2, sympy.solve([fn1, fn2]))
sympy.solve([fn1, fn2], x, y) #note: after fn have to mention all vars


#To find determinant

#det()
m = sympy.Matrix([[1, 2], [3, 4]])
determinant = m.det()
print(9, determinant)  # Output: -2

#can also use para
print(9.1, sympy.det(m))

#difference:

"""SymPy provides both options for user convenience:
Use sympy.det() for a more functional programming style where you pass the matrix explicitly.
Use .det() for an object-oriented style, working directly on the matrix object."""


#plotting using sympy
_ = sympy.plot(x**2, (x, -5, 5))
#using symbols
x = sympy.symbols("x")
_ = sympy.plot(sympy.sin(x), (x, -10, 10))


#for Taylor series expansion:
#series()
#sympy.series(expr, x, a, n, dir='+')
expr = (1/(1-x))  # Geometric series 
# but x**2 is not having more than 3 terms
x = sympy.symbols('x')
a = 5
n = 10
print(sympy.series(expr, x, a, n, dir='+'))