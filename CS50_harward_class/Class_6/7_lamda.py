#sorting a dict
#how? To sort you HAVE to specifying w.r.t which value to order

def get_data0(a):
    for i in sorted(a, key = ab): #the value is taken from specified fn return
        print(f"{i['name']} is in class {i['class']}")

#sorts according to 'wrt' specified
# the named parameter 'key' checks for dicts in list to sort wrt the specified key type
#here in a list, sort the list wrt the key "name"

def ab(a):
    return a["name"] #the index key "name" associated value is taken

import a6

get_data0(a6.create_dict())

#or (do not want to create a fn and, using sort only once)

def get_data1(a):
    for i in sorted(a, key = lambda b: b["class"]): #ignores use of: fn_name, pararenthesis, indent, return
        print(f"{i['name']} is in class {i['class']}")
get_data1(a6.create_dict())