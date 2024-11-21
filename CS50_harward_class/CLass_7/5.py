#don't want to reinvent the wheel?
#using lib that checks for patterns

import re

def a():
    a = input("enter: ")
    if re.search("@", a):     #(<pattern>, <str>, <flags = 0>)
        print("yes")
    else:
        print("no")


#want to set number of characters before/ after str?

#syn explain: 
# only "." = any character

#to set num of char:
# ".<symbol>" pair = number of repitions any characters before it.

#symbols:   
# "*" = 0 or more
# "+" = 1 or more
# "?" = 0 or 1
# "{m}"" = m rep
# "{m,n}"" = m to n rep


#note: .<symbol> does not mean only rep of same entered charac, but literally any charac like abc

#note: .<symbol><str> does not match, just check if no. of rep exists before str
      #<str>.<symbol><str> just checks if anywhere in str there exists a str then some rep cahrac then str

#extra
ab = "jvoie.ha@av@@v"
if re.search(r"h.?@", ab):
    print("\nyes\n")
else:
    print("\nno\n")

#syn(x):
#re.search("<any char = .>.<symbol><str>")


def charac_before():
    a = input("enter: ")
    if re.search(".+@.+", a):     #first arg = "<at least 1 charc><pattern>.<at least 1 charc>"
        print("yes")
    else:
        print("no")

#when nothing given before rep -> .rep
#how it works is until 1st pattern "@" encountered, checks character seq for first pattern, then 2nd pattern if exists

def email_check0():
    a = input("enter: ")
    if re.search(".+@.+..+", a):     #first arg = "<at least 1 charc><pattern>.<at least 1 charc><.= any char><at least 1 charc>
        #does not read . as "." so this line -> x <= 3 after @ as ".+" "." ".+"
        print("yes")
    else:
        print("no")


#to search a character that is unfortunately used in format structure
def email_check():
    a = input("enter: ")
    if re.search(r".+@.+\.com", a):     #using backslash to read "."     #need to put as raw string ("r") to tell py to not intepret "\" as usual way (\n or beggining and ending escape seq)
        print("yes")
    else:
        print("no")


def main():
    email_check()

main()

#note here it passes when the str exists => allows multiple duplicates
#this is a search fn so it is meant to check only if the entered str exists, then returns True 

#we use match to check exact patterns