#how to get integer input without entering in terminal?
def get_int(a): #by using argument
    while True:
        try:
            return int(input(a))
        except:
            pass
print(get_int("Enter:"))