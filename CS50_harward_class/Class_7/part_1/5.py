#re lib for common expressions
import re
searched= re.search("a", "bcdacba") #returns a Match object
print(searched) 
print(searched.start()) #return index of first character of 1st occurence
print(searched.span())  #returns tuple of start to stop match index
string = "abcde"
if re.search("a.e", "abcde"):
    print("2. Yes")
else:
    print("2. No")

string = "hibyehibye"
print(re.findall("^hibye$", string))

#using search -> span:
from re import search
text = "hello world"
a = search("o", text)
print(a)
b = a.span()
print(b)
text1 = text[0:b[0]] + "*" + text[b[0]+1:]
print(text1)

#using sub

def temp():
    result = re.sub(pattern, replacement, text, count=1)  # Replaces only the first match