#how to automate getting input using fn?
def get_int(a): #by using argument
    while True:
        try:
            return int(input(a))
        except:
            pass
print(get_int("Enter:"))