
import re
input1 = "https://twitter.com/benoitkuriakose"

if matched := re.search(r"^(?:https?://)?(?:www.)?twitter\..+/([\w_]+)$", input1, re.IGNORECASE):
    print("1. ", end = "")
    print(f"Username is: {matched.group(1)}")

#Additional features:
"""
re.splt() instead of splitting at character, can use or to have split at multiple values of characters
re.findall() find all the occurences of a pattern in a string
"""