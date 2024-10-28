a = "benoit"
#using special print (f) to use special format for print, curly brackets denote variable
print(f"hi {a}")

#py has built in funtions for string
a = " hello "
a = a.strip()
#strip removes all spaces at beginning and end of value
print(f"hi{a}")
#default value is whitespace
a = a.strip("h")
#removes all "h" only at end and beginning
print(f"hi{a}")

a = " hello "
a = a.rstrip()
print(a)
#removes whitespace to the right of str
#useful to not remove lines with only \n