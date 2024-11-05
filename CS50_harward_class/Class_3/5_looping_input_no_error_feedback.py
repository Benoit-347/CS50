#how to get only int input and if not ask again?
def get_int():
    while True:
        a = input("enter no of times to print hello:")
        try:
            a = int(a)
            print("hello\n"*a, end = "")
            return a
            #note: return also executes break along with returning (more powerful than break)
        except:
            pass
            # does an operation of intructing to continue the flow
            print("after pass print")

get_int()