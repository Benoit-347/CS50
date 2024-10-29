def write():
    with open('aa.csv', 'w') as file:
        file.write("Danush,B\nbenoit,B\nDeekshit,B\n")


def create_dict():
    write()
    c = []
    with open('aa.csv', 'r') as file:
        for i in file:
            a, b = i.rstrip().split(",")
            dict = {}
            dict["name"] = a.capitalize()
            dict["class"] = b
            c.append(dict)
    return c
