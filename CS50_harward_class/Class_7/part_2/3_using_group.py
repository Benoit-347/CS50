#group(<n>)     n: group_no
#used to get the nth group from match


#default is to return the entire match (the "0th group") as str

"""
difference bw group() and groups():
    groups() returns a tuple of values
    group() returns a str of the value
"""

#added features:
# 1. how to take both "abc, abc" and "abc,abc"
# 2. To take as many whitespacse bw names
import re
name = "Kuriakose, Benoit"
name = input("Enter name:")
matches = re.search(r"^(.+) *, *(.+)$", name)
#when using parenthesis (passed as argument in search parameter known as groups) the groups are then returned as elements of a tuple
if matches:
    last = matches.group(1)
    first = matches.group(2)
print("0. Before:\n", name, sep = '')
print("1.", first, last)
