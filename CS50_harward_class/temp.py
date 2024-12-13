import re
pattern = r"(\w+)hello\1hibro"
text = "abchelloabchibro"
match = re.match(pattern, text)

if match:
    print(match.group())  # Output: abc-abc
