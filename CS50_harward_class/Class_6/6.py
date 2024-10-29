def write():
    with open('aa.csv', 'w') as file:
        file.write("benoit,B\nDanush,B\nDeekshit,B\n")

write()

def create_dict():

    c = []
    with open('aa.csv', 'r') as file:
        for i in file:
            a, b = i.rstrip().split(",")
            dict = {}
            dict["name"] = a.capitalize()
            dict["class"] = b
            c.append(dict)
    return c

def printd(a):
    for i in a:
        print(f"{i['name']} is in {i['class']}")

#convert list of rows with nested coulumns to list of clolumns with nested rows:
#    c, d = [], []
#    for j in range(a[0]): attribute
#        for i in range(a): rows
#            b = a[i][j]
#            c.append(b)
#        d.append(c)
#    return d

def main1():

    printd(create_dict())

#or

def create_list():

    c, d = [], []
    with open('aa.csv', 'r') as file:
        for i in file:
            a, b = i.rstrip().title().split(",")
            c.append(a), d.append(b)
    a = [c, d]
    return a


def printd(a):
    for i in range(len(a[0])):
        print(f"{a[0][i]} is in {a[1][i]}")


def return_row(a):
    b =[]
    for j in range(len(a[0])):
        c = []
        for i in range(len(a)):
            c.append(a[i][j])
        b.append(c)    
    return b
    
def return_dict(a):
    b =[]
    for j in range(len(a[0])):
        c = {}
        c["name"] = a[0][j]
        c["class"] = a[1][j]
        b.append(c)    
    return b
print(return_dict(create_list()))    
            
        
def main2():
    printd(create_list())

main2()
