#palindrome using string traversing and concatenation
a = input("enter text to convert to palindrome: ")
n = len(a)
b = ""
for i in range(1, n+1):
    b = b + a[-i] #concatenate string
print("The reversed is:", b)
b = a+b
print("The required palindrome is:", b)