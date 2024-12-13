#By using flags
#1. re.IGNORECASE
#2. re.MULTILINE    #like paragraphs 
#3. re.DOTALL   #. with including newline
import re 
string = "HELLO.COM"
searched = re.search(r".+\.com", string, re.IGNORECASE)
if searched:
    print("1. Yes", searched.span())
else:
    print("1. No")
