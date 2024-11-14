#using csv lib to get advanced featues and no need to do corners, features manually
import csv
list1 = []
with open("8.csv", 'r') as file1:
    a = csv.reader(file1) #reading through the reader fn gives us the data formated according to all the corner cases
    for i in a:
        list1.append({"lab": i[0], "IA": i[1]})

print(list1)
