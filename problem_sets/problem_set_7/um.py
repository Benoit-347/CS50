import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    n = 0
    lower_str = s.lower()

    #Checking at the beggining of text
    len_str = len(lower_str)
    if len_str == 2:
        if lower_str[:2] == "um":
            return 1
    pattern = r"^um[ ,.?]"
    if re.search(pattern, lower_str):
        n +=1

    #Checking at the end of text
    if lower_str[-3:] == " um":
        n +=1

    ##Checking in between the text
    pattern = r" um[ ,.?]"
    i = 0

    
    while (i<len_str-1):    # i to maintain pos of last match
        lower_str = lower_str[i:]
        match = re.search(pattern, lower_str)
        if match:
            i = match.end()-1   # subtracting 1 To include spaces for next word
            n += 1
        else:
            break

    # Returning final count
    return n
if __name__ == "__main__":
    main()