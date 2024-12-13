import re
#using character classes with '/'
#/d -> decimal  equivalent to [0-9]
#/D -> complement of decimal
#/s  -> whitespace
#/w -> alphabets and numbers    equivalent to [a-zA-Z0-9]

#can use + after character classes as you would normally use

string = "hello2332325"
if re.search("\d+", string):
    print("1. Yes", re.search("\d+", string).span())
else:
    print("1. No")

#\w does not consider whitespaces like " " in its set
string = " "
if re.search("\w", string):
    print("1. Yes", re.search("\w", string).span())
else:
    print("1. No")