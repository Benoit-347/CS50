
import re
input1 = "https://twitter.com/benoitkuriakose"

matched = re.search(r"^(https?://)?(www.)?twitter\.com/(\w+)$", input1, re.IGNORECASE)

#multiple groups exist so we cont want to capture them?
# Use ?: to not capture that specific group
# mentioned at start of group

matched = re.search(r"^(?:https?://)?(?:www.)?twitter\.com/(\w+)$", input1, re.IGNORECASE)
if matched:
    print("1. ", end = "")
    print(f"Username is: {matched.group(1)}")

