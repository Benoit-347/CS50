# Display additional info of program on help flag.
# argparse, default shows usage info on all flags you add to it (eg -n N)
    # when adding arguments to parser_obj, we can assign a string to 'help' keyword, which on executing -h flag, display usage of tht particular flag.
        # pass string to 'description' keyword, which displays tht string, when -h flag is used. (Not attached to a now added flag, but displays in general space)
import argparse

# object creation
parser = argparse.ArgumentParser(description="Prints Meow")

# setup arguments to parse
parser.add_argument("-n", help= "N of times meow is printed", default= 2, type= int)    # shows the help keyword string, right next to the flag, when help is called.
                                                                                            # Additionally, specifying type, hard stores the data post of '-n' as int, rather than default str. Hence when accessing it now, we get and int, not requiring the int() converion.
                                                                                                # the default, specifies, what the number post, -n will hold, even if -n is not specified.
                                                                                                # python 3_b_arg_arse.py    will print Meow\nMeow\n     (even tho we skip -n entirely; shows what to do if -n is used as optional.)
# real parsing
result = parser.parse_args()    # returns a Namespace i.e. here, a obj with attributes.

if (result.n == None):      # in py, None is not equivalent to 0
    print("Meow")
else:
    # result.n returns int next to -n flag.
    print("Meow\n" * result.n, end = '')

"""
Output:
usage: 3_b_arg_parse.py [-h] [-n N]

Prints Meow

options:
  -h, --help            show this help message and exit
  -n N                  N times meow is printed
"""