#List input through index while reversing -> converting list to string
a = input("enter text: ")
n = len(a)
b = [None]*n #initialize data at index to make index exist
#reversing and adding data
for i in range(1, n+1):
    b[i-1] = a[-i]
c = ""
#converting list to string
for i in b:
    c = c+i
print(c)
