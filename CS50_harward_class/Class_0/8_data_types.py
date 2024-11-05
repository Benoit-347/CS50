#basic data types are: str, float, int, boolean

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