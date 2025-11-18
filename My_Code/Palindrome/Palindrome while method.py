#while loop, palindrome without string traversing
a = int(input("enter integer"))
d = a   #temp
c = 0   #store reversed
e = 0   #store no of digits by math.log10()
while d > 0:
    c = c*10
    b = d% 10
    c = (c + b)
    d = d//10
    e = e + 1

print("reversed:", c)
d = (a*(10**e)) + c
print("Palindrome:", d)