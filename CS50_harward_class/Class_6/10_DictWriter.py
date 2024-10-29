import csv
with open('10.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames= ['name', 'class'])
    writer.writeheader()
    writer.writerow({'name':"benoit", 'class': "B"})