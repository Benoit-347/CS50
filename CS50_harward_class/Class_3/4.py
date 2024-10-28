#how to get only int input and if not ask again?
while True:
    a = input("enter no of times to print hello:")
    try:
        a = int(a)
        print("hello\n"*a, end = "")
        break
        #stops current flow and exits loop and continues from there
    except:
        print("error,",a,"is not a integer, please enter integer value")
