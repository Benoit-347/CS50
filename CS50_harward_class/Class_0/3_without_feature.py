# 2 algos: 1. use print setting, 2. add str to geve output
a = "the string 1"
b = 100/2
c = 100//2

print(a, end = "")
print(" ", end = "")
print(b, end = "")
print(" ", end = "")
print(c)

print("\nAlgo 2:by type conversion and adding\n")

strb = str(b)
strc = str(c)
newa = a + " " + strb + " " + strc
print(newa)