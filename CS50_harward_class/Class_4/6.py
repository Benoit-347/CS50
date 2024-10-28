import sys
def a():
    sys.argv.remove(sys.argv[0])
    print(sys.argv)

#want to do with indexing instead? (slicing -> subset of a list)
a = [0, 1, 2, 3 ,4]
print("1", a[0:2])
print("2", a[1:])
print("3", a[-5:0])
print("4", a[0:5:-1])
print("7", a[-5:-1:-1])
print("5", a[-1:0:-1])
print("6", a[5:0:-1])
print("8", a[-1:-5:-1])

def b():
    print(sys.argv[1:])