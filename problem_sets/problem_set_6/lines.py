import sys

# check the number of cmd line args
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

# check if file is python (only last 2 char)
if not file_name.endswith(".py"):
    sys.exit("Not a Python file")

# trying to asscess file if it exists, else -> exit program
try:
    with open(file_name, 'r') as file1:
        lines = file1.readlines()
except:
    sys.exit("File does not exist")

# main program while accessing each line of file
no_of_lines = 0
for i in lines:

    i = i.strip()   # removes whitespace and if str is empty -> next i; also helps to check for comments
    if (not i):
        continue
    elif i[0] == "#":
        continue
    else:
        no_of_lines += 1


print(no_of_lines)
