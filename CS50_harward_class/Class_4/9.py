#using my user defined functions from other files
import my_fns
my_fns.check_input(5)


from my_fns import get_int
print("the input is:", get_int())

from my_fns import hello 
hello("you")

from my_fns import hello_argv
hello_argv()

from my_fns import cow_hello
cow_hello("benoit")