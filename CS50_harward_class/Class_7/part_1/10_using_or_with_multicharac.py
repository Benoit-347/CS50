import re 

#to check multiple charac instead of single, can't use set of characters method, so 
#You use groups denoted by "()"
#use operatios on a bunch of text with "()"

#check valid email
string = "abcd@gmail.ac.in" #allowing domain inside domain while also not affecting original
searched = re.search(r"\w+@\w+(\.\w+)?\.in", string)    #? makes it optional
if searched:
    print("1. Yes", searched.span())
else:
    print("1. No")

#to use this more standardly
#use or operator denoted by '|'
#syn: <pattern> = (<string1> | <string2>)
#string seperated by "|"
string = ".org"
searched = re.search(r"\.(org|com|in)", string)
if searched:
    print("2. Yes", searched.span())
else:
    print("2. No")
