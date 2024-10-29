#using csv lib to get advanced featues and no need to do corners, features manually
import csv
list1 = []
with open("8.csv", 'r') as file1:
    a = csv.reader(file1) #reading through the reader fn gives us the data formated according to all the corner cases
    for i in a:
        list1.append({"name": i[0], "class": i[1]})

def get_data1(ab):
    for i in sorted(ab, key = lambda b: b["name"], reverse=False): #reverse is optional
        print(f"{i['name']} is in class {i['class']}")
get_data1(list1)
