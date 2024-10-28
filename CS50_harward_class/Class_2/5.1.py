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

