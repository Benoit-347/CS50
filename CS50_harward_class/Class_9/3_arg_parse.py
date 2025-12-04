# Use module 'argpars' to use builtin way to parse flags from argv.
import argparse

# object creation
parser = argparse.ArgumentParser()

# setup arguments to parse
parser.add_argument("-n")

# real parsing
result = parser.parse_args()    # returns a Namespace i.e. here, a obj with attributes.

if (result.n == None):      # in py, None is not equivalent to 0
    print("Meow")
else:
    # result.n returns int next to -n flag.
    print("Meow\n" * int(result.n), end = '')