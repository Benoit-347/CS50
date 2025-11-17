#on vscode "run" runs the command "python <script.py>"
# this file script.py is loaded into a chache file.
# It is then complied into python bytecode. (python script to tokens; tokens parsed and compiled to bytecode)
# this bytecode contains instructins. All storage in pyhon is form of objects. Even the code is stored as PyCodeObject, with PyUnicodeObject- String; contains str size, ptr to the char arr and size of unicode storage for each char unit.
# Then it is interpretted and executed using Cpython interpretor

#interactive mode: This launches Python inside PowerShell
