import sys
#what if you enter no name or 2 words?
def error0(a = [5]):
    sys.argv = a
    print("Your name is:", sys.argv[1]) 
#error0()
#error0(["5.py", "benoit"])


 #to catch error you can use standard error handling

def error1(a = [5]):
    try:
        sys.argv = a
        print("your name is:", sys.argv[1])
    except IndexError:
        print("too few arguments")
print("start 1")
#error1()

#without tr except? how to know if it is empty? If we know how much is full
# if more than or less than a particular no of elements? Use len fn for seq

def main1():
    if len(sys.argv) < 2:
        print("too few arguments")
    elif len(sys.argv) > 2:
        print("too many arguments")
    else:
        print("your name is:", sys.argv[1])

#what if i do not want to continue to run the code and want to stop the 
#execution is b/w and terminate? So exit the program?

def main():
    if len(sys.argv) < 2:
        sys.exit("too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many arguments")
    print("your name is:", sys.argv[1])
main()
#want multiple inputs? use data type (list), (enter in  "") features to enter as string
