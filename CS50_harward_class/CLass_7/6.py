#putting start and end cases to limit extra char before and after req str

# "^" =  to match start of str
# "$" = to match end of str (or when newline exists: just before newline AT the end of str)
import re

def email_check():
    a = input("enter: ")
    if re.search(r"^.+@.+\.com$", a):     #using backslash to read "."     #need to put as raw string ("r") to tell py to not intepret "\" as usual way (\n or beggining and ending escape seq)
        print("\nValid\n")
    else:
        print("\nInvalid\n")
#notice here, it does not pass benoit@gmail.comAbc or benoit@gmail.com but, it passes benoit@gmailbenoit@gmail.com  and  also benoit@@.cogmail.com

email_check()