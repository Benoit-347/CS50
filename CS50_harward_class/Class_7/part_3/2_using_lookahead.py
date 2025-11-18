import re
url = "https://twitter.com/benoitkuriakose/profile/settings"
pattern = r"https?://.+\..+/(\w+)(?=/profile)"  #stops search before "/profile"
match = re.search(pattern, url)
print("3. ", end = "")
print(match.group(1))