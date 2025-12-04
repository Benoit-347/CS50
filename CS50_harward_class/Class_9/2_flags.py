"""
Passing args to program beside command to execute program- cmd line arg.
    It can also be used to control the behaviour (say for choosing 1 among n fns to use when executing) of our program, by using a convention called flags.

    python -n   // here -n denotes by convention a flag. So our program can just parse this and obtain the arg to a flag.
"""

import sys
if len(sys.argv) == 1:
    print("Meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    print("Meow\n"* int(sys.argv[2]), end = "")
else:
    print("Usage: python <file_name.py>")

"""
consider the scenario tht ur program has multiple flags to parse at same pos. You would simply use a seq of 'n' elif statments to check for 'n' types of flags (at same pos)
    Now what if you have optional flags, and if user skips the optional and writes next flags. The same pos may not be used.
        And what if you have combination of flags that are optional, a scenario like alternate flags may be input by the user. Parsing these would take some time to develop.
"""
