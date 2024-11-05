#using boolean in conditionals replacing its operators.(its operators also return boolean)
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False
def main():
    a = int(input("enter no to check"))
    if is_even(a):
        print(a, "yes")
    else:
        print(a, "no")
main()
#even 1/0 is same as True/ False
def is_even(a):
    if a % 2 == 0:
        return 1
    else:
        return 0
main()

a = []
if a:
    print("returned T")
else:
    print("returned F")