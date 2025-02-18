#say i want to print accoding to ranking, how do it?
b = 1
c = 2
a = [b, c]
for i in a:
    print(i)
print("end1")
#how to assign values to data with an custom index name and the value?
#dictionary (in curly braces)
#it is associating something with something else

dictionary_name = {"a":1, "b":2, "c":3} #key/index name, value pair
print(dictionary_name["a"]) #in traversing for the index int value we give the key name which takes
                            # the value associated with it
print("end2")
#what happens when i take elements through for loop?
for i in dictionary_name:
    print(i) 
    #takes the key name NOT value
print("end3")
for i in dictionary_name:
    print(i, dictionary_name[i]) #now gives the value associated as well