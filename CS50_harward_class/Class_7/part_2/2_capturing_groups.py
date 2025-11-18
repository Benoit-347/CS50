# how to get specific data from searched object?
# we use the feature of re lib 
# where you can specify groups that can be returned later

import re
name = "Kuriakose, Benoit"
matches = re.search(r"^(.+), (.+)$", name)
#when using parenthesis (passed as argument in search parameter known as groups) the groups are then returned as elements of a tuple
if matches:
    the_groups = matches.groups("nothing matched")
print("0. Before:\n", name, sep = '')
print("1.", the_groups)
first, last = the_groups
print("2.", last, first)

#this is known as capturing groups