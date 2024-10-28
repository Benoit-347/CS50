#q) WAP fn to print a box a lenght and breath using # per square unit
def square(a, b):
    for i in range(a):
        print("#"*b)
        
square(3,3)

def hollow_square(a, b):
    if a >=1:
        print("#"*b)
    if b>=2:    
        for i in range(1, a-1):
            print("#"+' '*(b-2)+"#")
    elif b>= 1:
        for i in range(1, a-1):
            print("#")
    if a >=2:
        print("#"*b)
hollow_square(5,5)