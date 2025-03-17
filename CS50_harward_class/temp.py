import random
l = []
for i in range(100):
    a =  random.uniform(0,0)
    l.append(a)
if 0 in l:
    print("yes")
elif True:
    for i in l:
        if i>0.99999:
            print("yes")
print(l)