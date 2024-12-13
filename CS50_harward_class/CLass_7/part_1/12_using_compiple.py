import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
text = "hi ph no : 123-456-7890"
print(re.search(pattern, text))
#using complile advantages:
#creates a reusable regex object, avoids recompiling the same pattern every time it’s used.
#feature: re.compile(r'\d+', re.IGNORECASE)