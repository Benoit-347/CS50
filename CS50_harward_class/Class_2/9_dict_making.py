def manual_list_to_dict():
    d = {}
    a = ["benoit", "deekshit", "dhanush", "madhan"]
    b = ["present", "absent", "absent", "preesnt"]
    for i in range(len(a)):
        d[a[i]] = b[i]
    print(d)
    return d

def dict(n):
    d ={}
    for i in range(n):
        d[input("enter key")] = input("enter value") #does value first then assgins to index so then does index
    print(d)
    return d
dict(3)