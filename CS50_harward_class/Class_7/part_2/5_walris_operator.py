# denoted by :=
# used in print and if

"""
in print()
To assign while printing
"""

print(a:= 3)

"""
in if
To assign from left to right (assign when right is True)
"""

import re
name = input("Enter name:")
print("0. Before:\n", name, sep = '')
if matches := re.search(r"^(.+) *, *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print("1.", name)

