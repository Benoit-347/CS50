#features of putting "" when entering comma and input each row
def acsv():
    import csv
    a, b = input("enter1"), input("enter2")
    with open('10.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["1","2"])
        writer.writerow([b,a])

#the manual will be

def manual():
    a, b = input("enter1"), input("enter2")
    with open('10.csv', 'w') as file:
        c = []
        c.append(["1","2"])
        c.append([a,b])
        file.write(write_it(c))

def write_it(a):
    b= ""
    for i in a:
        c = ''
        for j in i:
            c = c + str(j) + ','
        b = b + str(c[:-1]) + '\n\n'
    return b
manual()