#need to change flow when error occurs:
try:
#executs normally (makes note that in case error return except block)
    a = int("hi")
#if error occurs in above line then variable a value is not initiated and assigned as error broke the process
except:
#This is mandatory, not optional
    print("error has occured")
#note: try is not a function, it is a statement