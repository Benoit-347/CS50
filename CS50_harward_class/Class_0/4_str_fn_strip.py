a = "benoit"
#using special format of string (f) to then return and print, curly brackets denote variable
print(f"hi {a}")

#almost all characters not in curly braces in taken as str

#py has built in funtions for string. 
# 1) removing specified characters at beggining or end

a = " hello "
a = a.strip()
#default value is whitespace
#strip removes all whitespaces at beginning and end of value


print(f"1. hi{a}")
a = a.strip("habc")
#removes any character mentioned in strip from only at end and beginning
print(f"2. hi{a}")


a = " hello   \n\n"
a = a.rstrip()
print(f"3. {a}")
#removes whitespace to the right of str
#useful to not remove lines with only \n

a = "\nhi hello   \n\n"
a = a.rstrip()
print(f"4. {a}")