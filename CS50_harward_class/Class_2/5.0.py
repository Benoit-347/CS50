#how to get raminder:%
a = int(input("enter no"))
n = a%5
print("remainder when divided by 5 is:", n)

def main():
    x = int(input("enter number to find if even or odd:"))
    is_even(x)

    
def is_even(a):
    if a %2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")
main()