#Palindrome using for loop only
import math
a = int(input("enter number"))
#number of digits
b = int(math.log10(a)//1 +1)
c = a #temp
d = 0 #store reversed
f = 0 #count digits with math.log10()
for i in range(b):
    d = d*10
    e = c% 10
    d = (d + e)
    c = c//10
    f = f + 1
print("reversed is:", d)
c = a*(10**f)+d
print("Palindrome is:", c)