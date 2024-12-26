dict1 = {"UID":{"name":"benoit", "house": "red"}}
#if UID unknown
for i in dict1:     # searches through all keys so: n complexity
    if i["name"] == "benoit":
        dict1[i]["house"] == "blue"

#if UID is known:
if "UID" in dict1:
    if dict1["UID"]["name"] == "benoit":
        dict1["UID"]["house"] == "red"