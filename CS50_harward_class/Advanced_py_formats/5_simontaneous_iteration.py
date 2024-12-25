l1 = [1,2]
l2 = [11,22]
for i,j in l1, l2: #unpacts first element of this immutable seq l1, l2 then next element.
    print(i,j)

l1 = [1,2,3,4]
l2 = [11,22,33,44]
print("\n2.\n")
try:
    for i,j in l1, l2: #unpacts first element of this immutable seq l1, l2 then next element.
        print(i,j)
except:
    print("Error faced\nExcept block:")
    for i,j,k,l in l1, l2:
        print(i,j,k,l)



#iterating over two data sets at the same time
#use zip()
print("\n3.\n")
for i, j in zip(l1,l2):
    print(i,j)

#when diffent sequence lengths stops at shortest length

l1, l2 = [1,2,3,4], [11,22,33]
print("\n4.\n")
for i,j in zip(l1,l2):
    print(i,j)