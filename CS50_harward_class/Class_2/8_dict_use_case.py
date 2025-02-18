#how to potray data with more than 1 value? With multiple values multiple names for the values exist
#make a list with nested dictionary associating value name and value with each row seperated by different dictionary

a = [{"name":"benoit", "rank":2, "game":"english"},
     {"name":"betina", "rank":1, "game":"handwriting"}
]
# 2 D dictionary
for i in a:
    print(i["name"], "rank:", i["rank"], i["game"])
    #takes element(the dict1) and value asssociated with index name of "name" in element is benoit