import re
ab = "jvoie.ha@av@@v"

def a():
    if re.search(r"h.?@", ab):
        print("\nyes\n")
    else:
        print("\nno\n")

def email_check():
    a = input("enter: ")
    if re.search(r".+@.+\..+", ab):     #using backslash to read "."     #need to put as raw string ("r") to tell py to not intepret "\" as usual way (\n or beggining and ending escape seq)
        print("yes")
    else:
        print("no")
a()