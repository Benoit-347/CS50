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
# only "." = any character except newline

#to set num of char:
# "<any_char><symbol>" pair = number of repitions to the character before it.

#symbols:   
# "*" = 0 or more
# "+" = 1 or more
# "?" = 0 or 1
# "{m}"" = m rep
# "{m,n}"" = m to n rep


#syn(x):
#re.search("<any char = .>.<symbol><str>")


def charac_before():
    a = input("2. enter: ")
    if re.search(".+@.+", a):     #first arg = "<at least 1 charc><pattern>.<at least 1 charc>"
        print("2. yes")
    else:
        print("2. no")

"""
IMPORTANT: .+a -> checks for the last occurence of 'a' not first 
beautiful thing: .<range_rep> makes the search() fn so when true, continues searching until next str pattern is met or False. For findall as well splits to string only when interuppted by False
range_rep are: . * {m-n} ?
when nothing given before rep -> .rep
how it works is until 1st pattern "@" encountered, checks character seq for first pattern, then 2nd pattern if exists
"""
#eg:
def email_check0():
    a = input("3. enter: ")
    if re.search(".+@.+..+", a):     #first arg = "<at least 1 charc><pattern>.<at least 1 charc><.= any char (only one)><at least 1 charc>     imples at least 3 char after @
        #does not read . as "." so this line -> x <= 3 after @ as ".+" "." ".+"
        print("3. yes")
    else:
        print("3. no")


#note: .<symbol> does not mean only rep of same entered charac, but literally any charac like abc

#to search a character that is unfortunately used in format structure
def email_check():
    a = input("4. enter: ")
    if re.search(r".+@.+\.com", a):     #using backslash to read "."     #need to put as raw string ("r") to tell py to not intepret "\" as usual way (\n or beggining and ending escape seq)
        print("4. yes")
    else:
        print("4. no")


def main():
    email_check()

main()

#note here it passes when the str exists => allows multiple duplicates
#this is a search fn so it is meant to check only if the entered str exists, then returns True 

#we use match to check exact patterns




#note: .<symbol><str> does not match, just check if no. of rep exists before str
      #<str>.<symbol><str> just checks if anywhere in str there exists a str then some rep cahrac then str

#extra
ab = "jvoie.ha@av@@v"
if re.search(r"h.?@", ab):
    print("1. \nyes\n")
else:
    print("1. \nno\n")