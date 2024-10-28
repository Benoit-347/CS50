#how to create your own functions to customize or organize or create structure or automate code:
def a(b): #syn def-> keyword, a->function name, (), (optional)enter argument name to use only in def block
         #only to show work to do in statements block
    print(b, "hi")
a("benoit")

#in detail

a = "ben"
def hello(b):
#helps define our own function
#lines after colon means everything indented (in the same block) is part of the fn
    print(b)
#shows what to do with var b in argument    
hello(a)
#argument entered is copied to b in the defined fn
def hello(b="world"):
#gives default value as str world    
    print(b)
hello()