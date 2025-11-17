import os, sys, csv
if len(sys.argv) != 3:      # check if args passed are enough
    sys.exit(1)
file_1 = sys.argv[1]
file_2 = sys.argv[2]

if file_1 not in os.listdir():  # check if input file exists
    sys.exit(1)

with open (file_1, 'r') as file1:
    with open (file_2, 'w') as file2:
        reader1 = csv.reader(file1)
        writer1 = csv.writer(file2)
        read = list(reader1)[1:]    # removes the header to foramt names

        final_list = [["first", "last", "house"]]   #adds header before hand
        for line in read:
            name = line[0]
            name.replace('"', '')   #removers the quotes in each name cell
            print(name)
            last, first = name.split(', ')  # removes and splits to get each first and last name
            new_list = [first, last, line[1]]   # this represents each row
            final_list.append(new_list)
        writer1.writerows(final_list)

