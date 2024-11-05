# using advanced form of returning boolean with conditionals:
def is_odd(a):
    return True if a % 2 == 1 else False
def main():
    a = int(input("enter num"))
    if is_odd(a):
        print("y")
    else:
        print("n")
main()
#making it shorter as comparison only gives true or false
def is_odd(a):
    return a % 2 ==1
main()