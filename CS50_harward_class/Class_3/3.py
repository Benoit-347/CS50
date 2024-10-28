#can we write conditions in except?
a = int(input("enter value"))
try:
    int(a)
except NameError:
#Executes only when error returned is ValueError
    print("NameError block executed")
except ValueError:
    print("(condition worked, multiple except when error out of subset) error has occured")
except:
    print("neither name or value error")
#remember except is executed only when the condition that error has returned
else:
#executes after try block when no above except conditions are met
    print("else block is printed")