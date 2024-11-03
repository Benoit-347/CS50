def get_valid1():
    while True:
        a = input("enter: ")
        if "@" in a and "." in a:
            b1, b2 = a.split("@")
            c1, c2 = a.split(".")
            if b1 != "" and b2 != "" and c1 != "" and c2 != "":
                print(a, "validated")
                break

def get_valid2():
    while True:
        a = input("enter: ")
        if "@" in a and "." in a:
            b1, b2 = a.split("@")
            c1, c2 = a.split(".")
            if b1 and b2 and c1 and c2:
                print(a, "validated")
                break

