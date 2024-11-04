#errors when accesing global var in local scope
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