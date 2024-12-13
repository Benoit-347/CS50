url = "https://twitter.com/benoitkuriakose"
import re
match = re.search(".+/(\w+)$", url)
print("1. ", end = "")
print(match.group(1))

#type 2
import re
url = "https://twitter.com/benoitkuriakose/profile/settings"
pattern = r"\..+/(\w+)"
match = re.search(pattern, url)
print("2. ", end = "")
print(match.group(1))

# (\w+) captures the final part after the last /

import re
url = "https://twitter.com/benoitkuriakose/profile/settings"
pattern = r"https?://[^/]+/(\w+)"
match = re.search(pattern, url)
print("3. ", end = "")
print(match.group(1))