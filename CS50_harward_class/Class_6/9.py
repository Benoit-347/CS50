#assigning coulomns to reader by dictreader and mentioning colounm name in first row of csv
import csv
list1 = []
with open("9.csv", 'r') as file1:
    a = csv.DictReader(file1) #creates a local var a as dict with coloumn name as keys
    for i in a:
        list1.append({"name": i['thename'], "class": i['theclass']})
def get_data1(ab):
    for i in sorted(ab, key = lambda b: b["name"], reverse=False): #reverse is optional
        print(f"{i['name']} is in class {i['class']}")
get_data1(list1)

#note here that the dict reader returns a seq of dicts for each row, so notice line 6
list1 = []
with open("9.csv", 'r') as file1:
    a = csv.DictReader(file1) 
    for i in a:
        list1.append(i)
        print(i)