import re
string = ".org"
non_capturing = "(?:<str>)"
searched = re.search(r"\.(org|com|in)", string)
if searched:
    print("2. Yes", searched.span())
else:
    print("2. No")