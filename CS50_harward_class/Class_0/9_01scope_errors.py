#errors when accesing global var in local scope
def using_replace():
    try:
        a = a.replace(" ", "*") #cannot modify the global variable by local (unless declared global) (UnboundLocalError)
        print(a)
    except:
        print("cannot modify the global variable by local (unless declared global) (UnboundLocalError)")
        try:
            print(a)
            a = 0   #If you attempt to access it before assigning a value, Python will raise UnboundLocalError
            print(a)
        except:
            print("cannot print global when assigning in later lines, so then loses access to global from local")
a = "hello world"
using_replace()