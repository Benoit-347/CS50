
# list vs dict

"""
list = [1,2,3,4]
accessed by 0,1,2,3
dict = {'benoit':1, 'harry:' 2, 'panda': 3, 'someone': 4}
accessed by 'benoit', 'harry', 'panda', 'someone'

difference:
while iterating over them:
lists return the iterable values
dicts return the dict (index) keys
"""

# dict data type features:

"""
can access values only by using keys (or dict.values())
can acess keys only by using iterrations (or dict.keys())
extra: assgining values to keys when it does not exist .setdefault(), .get(), .items()
"""

# using these features:

"""
use of {"benoit": "red"} vs {"name": "benoit", "house": "red"}
# in a database we want the data related to a student -> search wrt name: store key as benoit value as data
# in a database we want to store such that need name to be used later as well, -> store key as a UID and value as data including benoit
"""
# when we use list/tuples, we often can make mistakes when using indexes so it may be better to use dicts

students = {"Harry":"gryffindor", "panda":"ravenclaw"}  # the seach obj cannot be found, other than with ,keys() fn on dict.
for i in students:
    if i == "Harry":
        students[i] = "Gryffindor"
    print(f"{i} is in {students[i]} house")


#here as lenght of dict increases the num of iterations also increase so dont use keys to store values that need to be searched

# use:

print(students["Harry"])    

#or:
students = {"Harry":{"name":"Harry", "house":"gryffindor"}, "panda":{"name":"panda","house":"ravenclaw"}}
print(students['Harry'], students["panda"], sep = '\n')

#use unique ID instead of names if req