#don't want to reinvent the wheel?
#using lib that checks for patterns

import re

def a():
    a = input("enter: ")
    if re.search("@", a):     #(<pattern>, <str>, <flags = 0>)
        print("yes")
    else:
        print("no")

#want to set number of repititions of character before/ after str?
# "*" = 0 or more
# "+" = 1 or more
# "?" = 0 or 1
# "{m}"" = m rep
# "{m,n}"" = m to n rep

def charac_before():
    a = input("enter: ")
    if re.search(".+@.+", a):     #first arg = ".<repeat type><pattern>.<repeat type>"
        print("yes")
    else:
        print("no")

def email_check0():
    a = input("enter: ")
    if re.search(".+@.+..+", a):     #does not read . as "."
        print("yes")
    else:
        print("no")

email_check0()

def email_check():
    a = input("enter: ")
    if re.search(r".+@.+\..+", a):     #using backslash to read "."     #need to put as raw string ("r") to tell py to not intepret "\" as usual way (\n or beggining and ending escape seq)
        print("yes")
    else:
        print("no")

email_check()
