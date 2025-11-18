# match() 
# -> to start check at beginning of string only
# like search but does not require ^ at start of a string

#fullmatch()
# -> to start check at beginning of string until end of string
# like search but does not require ^ at start of a string AND $ at end of string

#why?
#1. easier to understand (does not require to put ^ and dollar)
#2. more efficient as stops processing as soon as a match is determined (from the start of the string), 
# making it slightly more efficient than re.search() with both ^ and $

import re
string = "abcd@gmail.ac.in" #allowing domain inside domain while also not affecting original
searched = re.search(r"^\w+@\w+(\.\w+)?\.in$", string) 
#using match
searched = re.fullmatch(r"\w+@\w+(\.\w+)?\.in", string)    
if searched:
    print("1. Yes", searched.span())
else:
    print("1. No")