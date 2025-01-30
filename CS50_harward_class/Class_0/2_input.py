
#what is return?

#by taking instructions you can do operations, but to hand back a product after operations is called return
#not to be confused to changes made to existing data

#manually entering values into program is problem? Enter values through terminal


a = input("enter the input 1") #input fn returns the data you put in the terminal
#the variable takes the data you put in the terminal


# doing operations in str
name = input("enter the input 1, the data should be put along with print")
# note: the spaces registers to give the ouput as spaces in the strings
print("printed1" + name)



#we run -> run from script.py but using input -> taking data outside of scipt 
# (script buffer > compiled to py bytecode > interpretted > interupts terminal > prompts input from terminal > continue execution)


#so can pass input during running as well(not in script) by using sys module: sys.argv[<nth term>]


#multiline input
import sys
the_input = sys.stdin.read()

