#reading a csv file and outputing its value
def write():
    with open('aa.csv', 'w') as file:
        file.write("benoit,B\nDanush,B\nDeekshit,B\n")

write()

with open('aa.txt', 'r') as file:
    full_read = file.readlines()
    for each_line in full_read:
       spiltted = each_line.rstrip().split(",")
       print(f"{spiltted[0].capitalize()} is in class {spiltted[1]}")