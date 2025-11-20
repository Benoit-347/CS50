#on vscode "run" runs the command "python <script.py>"
# this file script.py is loaded into a chache file.
# It is then complied into python bytecode. (python script to tokens; tokens parsed and compiled to bytecode)
# this bytecode contains instructins. All storage in pyhon is form of objects. Even the code is stored as PyCodeObject, with PyUnicodeObject- String; contains str size, ptr to the char arr and size of unicode storage for each char unit.
# Then it is interpretted and executed using Cpython interpretor

# NOTE: since python uses pybytecode which has 50ns overhead for each statement (py is intepretoer lang) (more precise is: number of bytecode ops in program)
            # lesser number of statements executed in a program is the most basic way to see runtime speed.
        # use of use of optimized C-level primitives (builtins, numpy) 
            # also c-level fns like str(long_number), list(), int(); min(), max(), sum()
"""
Core builtins implemented in C

len, abs, pow, round, divmod, min, max, sum, any, all, sorted (calls into C timsort), reversed, enumerate, range, zip, map, filter, next, iter, eval (interpreter hook but C frames), print (C builtin), isinstance, issubclass, hash, id, type, vars, globals, locals (C implemented accessors).

int, float, str, bytes, bytearray, list, tuple, set, dict, complex — type constructors and many of their basic operations are C.

operations on sequencial data types:

    list: .append, .extend, .pop, .insert, .remove (some behaviors in C), .sort() (timsort in C), .reverse(), slicing implementations.

    dict: __setitem__, __getitem__, .get, .pop, .update, .keys()/.items()/.values() (views are C objects), fast hashing & lookup internals.

    set: .add, .remove, .discard, set algebra operations (|, &, -).

    str: .find, .rfind, .replace, .join, .split (split has Python wrapper but heavy work in C), .encode, .format internals (formatting engine mostly C).

common Library fns for optimization:    

itertools — all iterator primitives (chain, islice, tee, permutations, combinations, accumulate, etc.) are implemented in C and extremely fast.

math — all math functions (sin, cos, sqrt, log, factorial, etc.) are C wrappers to libm or C code.


"""
#interactive mode: This launches Python inside PowerShell
