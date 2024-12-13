#using dynamic pattern searching 

import re
pattern = r"(\w+)hello\1"
#here \1 means reference to first group
text = "abchelloabc-!@a"
match = re.match(pattern, text)

if match:
    print("1.", match.group())  
# Output prints entire matched string

#used to: Identify strings with repeated sections, such as duplicate words or numbers.
#sep not req

pattern = r"(\w+)\1"
text = "hellohellohello"
match = re.match(pattern, text)

if match:
    print("2.", match.group()) 

# Group referencing helps validate structured data formats like 
# palindromes, mirrored strings, or other patterns with symmetry.