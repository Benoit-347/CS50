#don't want to reinvent the wheel?
#using lib that checks for patterns

import re

def a():
    a = input("enter: ")
    if re.search("@", a):     #(<pattern>, <str>, <flags = 0>)
        print("yes")
    else:
        print("no")

#want to set number of repititions?
# "*" = 0 or more
# "+" = 1 or more
# "?" = 0 or 1
# "{m}"" = m rep
# "{m,n}"" = m to n rep

a = input("enter: ")
if re.search(".+@", a):     #first arg = ".<repeat type><pattern>"
    print("yes")
else:
    print("no")
