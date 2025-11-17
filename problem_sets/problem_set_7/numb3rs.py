# searching for 4 blocks of 3 digits then grouping them. Check each group to lie in range at range of 0 and 255.

import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip)    # get mathes in groups

    if matches:
        #check first octet
        if not (int(matches.group(1)) > 0 and int(matches.group(1)) <= 255):
            return False

        #check remaining octet
        for i in range(2,5):    #iterating over each group thorugh iterations
            if not (int(matches.group(i)) >= 0 and int(matches.group(i)) <= 255):
                return  False
        else:       # control comes here when the whole loop runs until its condition hit false
            return True
        #returns False if no match
    return False

if __name__ == "__main__":
    main()
