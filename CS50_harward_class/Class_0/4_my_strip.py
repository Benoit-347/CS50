#pseudocode:
"""
. 1st argument = text, 2nd = strip pool
1.
. iterate over text from beginning, until the i character is outside strip pool skip concatenating
. when outside character encountered pass flag to start concatenating 
2. take reverse of left stripped  and iterate as done before
. return the reverse of it to get back normal but stripped text

"""

def strip_it(a, b):
    total = ""
    flag = 0
    for i in a:
        if flag ==0:
            if i in b:
                continue
            else:
                flag = 1
        total += i
    total_reverse = total[::-1]
    result = ""
    flag1 = 0
    for i in total_reverse:
        if flag1 ==0:
            if i in b:
                continue
            else:
                flag1 = 1
        result += i
    return result[::-1]
print(strip_it("aaahelloaaa", "a"))