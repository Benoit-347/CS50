#when we suddenly want to define functions we do it in the latest line(bottom), but to use it, it has to be defined above use, so we define main to structure flow and define fn at latest while still being useful
def main():
    a = input("enter name")
    b = a*5
    hello(b)
def hello(b):
    print("hello", b)
main()