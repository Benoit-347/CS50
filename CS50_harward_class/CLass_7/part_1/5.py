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