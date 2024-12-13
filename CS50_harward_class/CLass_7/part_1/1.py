#how to check/validate input
def get_valid1():
    while True:
        b = 0
        a = input("enter: ")
        for i in a:
            if i == "@":
                print("validated")
                b = 1
                break
        if b ==1:
            break

#better code:

def get_valid2():
    while True:
        a = input("enter: ")
        if "@" in a:
            print("validated")
            break
get_valid1()