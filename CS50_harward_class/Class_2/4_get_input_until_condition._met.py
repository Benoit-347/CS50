#how to keep asking input until positive integer
#0 is even but not positive
while True:
    n = int(input("enter:"))
    if n>0:
        break
for _ in range(n): #_ to denote the value in range is temporary and no used later 
    print("hello")
