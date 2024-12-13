# To define what chareacters are allowed or by what characters are to be excluded

# [] = set of characters
# [^<seq of characters>] = complementing this set is allowed

#here to define, the "."" in ".<symbol>" is replaced by "[]" or "[^<seq of characters>]"

import re

def email_check():
    a = input("enter: ")
    if re.search(r"^[^@]+@[^@]+\.com$", a):     #using backslash to read "."     #need to put as raw string ("r") to tell py to not intepret "\" as usual way (\n or beggining and ending escape seq)
        print("\nValid\n")
    else:
        print("\nInvalid\n")

#notice here, it does not "passbenoit@gmailbenoit@gmail.com" or "benoit@@.cogmail.com" but, it passes "benoit.@gmail.com"  and  also "benoit @gmail . com"

# there are a lot of unknown existing values when we use complement set (= universal - set) so we need to define what the valis is.

#key to define range of alpa or num: [<first alpha by order> - <till end alpha by order>]

def email_check_V2():
    a = input("Enter email to validify: ")
    if re.search(r"^[a-z]+@[a-z]+\.com$", a):   #[a-z]
        print("\nValid\n")
    else:
        print("\nInvalid\n")

def main():
    email_check_V2()

main()