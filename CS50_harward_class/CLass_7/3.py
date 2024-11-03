def get_valid3():
    while True:
        a = input("enter: ")
        if "@" in a:
            b1, b2 = a.split("@")
            if b1 and "." in b2:  
                c1, c2 = b2.split(".")
                if c1 and c2:
                    print("valid")
                    break

#checks entered domain is ".edu"
def get_valid3a():
    while True:
        try:
            a = input("enter: ")
            if "@" in a:
                b1, b2 = a.split("@")
                if b1 and "." in b2:  
                    c1, c2 = b2.split(".")
                    if c1 and c2[-3:] == "edu":
                        print("valid")
                        break
        except:
            print("enter one @ and . while ending with .edu")

def get_valid3b():
    while True:
        a = input("enter: ")
        if "@" in a:
            b1, b2 = a.split("@")
            if b1 and b2.endswith(".edu"):
                print("valid")
                break
get_valid3a()
#use lib to reduce manual effort for standard expressions