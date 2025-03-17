import sys
from pyfiglet import Figlet

def exit():
    sys.exit(1)

sys_arg = sys.argv
length = len(sys_arg)

if length == 1:
    Input = input("Input: ")
    print(f.renderText(Input))

elif length == 3:   #when provided 2 arguments

    if (sys_arg[1] == "-f" or sys_arg[1] == "-font"):   #Check first aegument
        try:
            f = Figlet(font = sys_arg[2])   #check second argument
        except:
            exit()
        Input = input("Input: ")
        print(f.renderText(Input))
    else:
        exit()

else:
    exit()
