# denoted by :=
# used in print and if

"""
in print()
To assign while printing
"""

print("1.", a:= 3)

"""
in if
To assign from left to right (assign when right is True)
"""

import re
name = 'benoit'
if i := re.search(("benoit"), name):
    print("2.", i.group())

#when using normal analogy
if n := "benoit" == name:
    print("3.", n)  # output:3. True
    
# -> can be used when right side returns True and return a value you want to assign