#data type subset category
a = "hi"
# int is subset of float is subset of string
try:
    int(a)
except:
#try always requires except block
    try:
     float(a)
    except:
     str(a)
#type function
print(type(a))
print("hi", type("hi").__name__)

def using_replace():
    try:
        a = a.replace(" ", "*") #cannot modify the global variable by local (unless declared global) (UnboundLocalError)
        print(a)
    except:
        try:
            print(a)
            a = 0   #If you attempt to access it before assigning a value, Python will raise UnboundLocalError
            print(a)
        except:
            print("reached except")
using_replace()