# re.sub()
# like a replace fn but can do mor with re lib
# syn: sub(pattern, replacement_to, from_string)
import re
input1 = "https://twitter.com/benoitkuriakose"

def get_username1(text):
    username = re.sub(r"^(https?://)?(www.)?twitter\.com/", "", text)
    return username

print("1. ", end = "")
print(get_username1(input1))
input2 = "https://twitter.com"
print("2. ", end = "")
print(get_username1(input2)) #output is a link

#so in re to avoid debug rabbit hole, do complexity incrementally
matched = re.search(r"^(https?://)?(www.)?twitter\.com/(\w+)$", input1, re.IGNORECASE)
if matched:
    print("3. ", end = "")
    print(f"Username is: {matched.group(3)}")

