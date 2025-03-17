#command-line arguments
import sys
#sys argv -> argv takes the input while executing the code. 
# this is a variable, 
# which is also a list
print(sys.argv)

#notice that after python syntax even the input argument of file name is taken
#as this is a list, you can use list features as well
def print1():
    print(sys.argv[1])
print1()

#notice, the characters are seperated by space
#by running with double space you can notice that it works like it used 
#split at character "space"
#note: at terminal: intepreter file_name input
#no input? what happens when no element in list when indexed? IndexError