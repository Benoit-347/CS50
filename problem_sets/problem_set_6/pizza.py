import sys, tabulate, csv

# check the number of cmd line args
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

# check if file is python (only last 2 char)
if not file_name.endswith(".csv"):
    sys.exit("Not a CSV file")

# trying to access file if it exists, else -> exit program
try:
    with open(file_name, 'r') as file1:
        lines = list(csv.reader(file1))     # converting to list format with restpect to csv
        print(tabulate.tabulate(lines, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
