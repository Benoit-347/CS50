# if in for lists, then append if not in
# equivalent in 1 statement push -> set -> add();
# backend of a set is a hashed units into a table, each add or remove hashes and chks, and does op; all in ~ 1 opcode object.
    # any access to global var can be done anywhere. But modifying to global can only be done, when write 'global' statement.

"""
To communicate between functions in a program in Python we can use Global variables, but these are supposed be used very sparingly as the difficult to track their food. We have to use a special Gateway that is classes. The option of using variables through function parameters to change the original variable is not an option for using functions would change only the local variables not a fitting the original variable. 

Classes will act as a common message point between multiple functions. And classes themselves have operations you can perform on its data that it holds called methods.

Inter function communication in Python therefore only uses classes instead of global variables (globals are used in nichie scenarios tho, like a consumer producer simple code; although  this uses a common file/section very like classes).
Classes takes advantage of object encapsulation, being different from global and access a object space only by its self.

You can also take advantage of nested defined fns to control local scope and shared local scope, Why use this? It's cleaner than a class if you just need one specific piece of shared state.
Correction: You can pass and use obj references in py;
Mutable Types (Lists, Dictionaries, Objects): You can change the original variable. If you pass a list to a function, and the function appends to it, the original list is modified.

This means you can use function parameters for communication, but only if you wrap your data in a "Mutable Container" (like a list or dict).

python is not strongly typed, hence you cannot force a varible to be of a certain type, the intepretor does it for you.
    But you can provide "hints" to the postfix of a variable, to show a developer, what data type a var expects (a py itpretor ignores this; like a comment; Use mypy <file.py> instead of pyton <file.py> to validate these hint errors.)
Eg usage-
a: int = 10
l: list = [1, 2, 3, 4, 5]
s: string = "Orange"


Doc strings:- the comments/ string right below a fn, it has a feature of when a user writes help(fn) displays that doc string.
Syn:
def meow(n):
    ""' This is a docstring
        :param: n count
        :type n: int
        :return: a str of meows
        :rtype: a str

Passing args to program beside command to execute program- cmd line arg.
    It can also be used to control the behaviour (say for choosing 1 among n fns to use when executing) of our program, by using a convention called flags.

    python -n   // here -n denotes by convention a flag. So our program can just parse this and obtain the arg to a flag.

    
"""
