def check_input(a):
    try:
        b = int(a)
        print(a, 'is int')
    except: 
        try:
            c = float(a)
            print(a, 'is flo')
        except:
            try:
                str(a)
                print(a, "is stri")
            except:
                print("error: neither int, float or str")

def get_int(a="(default argument) Enter:"): #by using argument
    while True:
        try:
            return int(input(a))
        except:
            print("not int")
            pass

def is_prime(n):
    if n == 1 or n == 0 or n == -1:
        print("Neither prime or composite")
    else:
        for i in range(2, n):
            if n % i ==0:
                print(n, "is a prime number")
                break
        else:
            print(n, "is not a prime number")

def hello(a = "world"):
    print("hello", a)

def hello_argv():
    import sys
    if len(sys.argv) == 2:
        print("hello", sys.argv[1])
    else:
        print("len not right")
        
def cow_hello(a="world"):
    import cowsay
    b = "Hello " + a
    cowsay.cow(b)
if __name__ == "__main__": #make sure to put __main__ in str
    check_input("5")
    print("num is:", get_int("enter"))
    is_prime(945)
