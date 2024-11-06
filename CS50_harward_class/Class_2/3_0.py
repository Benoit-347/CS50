#lists

#A list is a data structure in Python that is a mutable, ordered sequence of elements

#2. order
#The first item is at index 0, the second at 1, and so forth.

#3. hetero and homo type
# While Python lists are commonly homogeneous (storing elements of the same type, they can also hold mixed data types as well (heterogeneous).

#4. Dynamic Sizing
#Lists in Python do not need a predefined size, as they can grow and shrink dynamically.
data = [5, 6, 3, "hi"]  #index: 0,1,2,3
data = (5, 6, 3, "hi")
data = list(data)
print(data)

#traversing
print(data[1])

#slicing
a = data[0:3:1]     #start stop increment

#removing elements: del statement
l1 = [1,2,3,4,5]
del l1[2]
print(f"del: {l1}")

l1 = [1,2,3,4,5]
#list fns

#0 index, len

def most_basic_used():
    print(f"len of l1 is: {len(l1)}")
    print(f"index of 2 is: {l1.index(2)}")      # <list>.index(<value>)

#1 append
def append1():
    print(f" append: {l1.append(data)}")

#2 extend()
def extend2():
    print(f" extend: {l1.extend(data)}")

#3 insert()
def insert3():
    l1.insert(5, data)      # <list>.insert(<index>, <value>)
    print(f" insert: {l1}")     

#4 pop()
def pop4():
    l1.pop(1)     # <list>.pop(<index>)
    print(f"pop: {l1}")   

#5 remove()
def remove5():
    l1.remove(1)     # <list>.remove(<value>)
    print(f"remove: {l1}")   

#6 reverse()
def reverse():
    l1.reverse()     # <list>.reverse()
    print(f"reverse: {l1}")

#7 sort()
def sort7():
    l1.sort(reverse = True)     # <list>.sort(reverse = <True/False>)
    print(f"sort: {l1}") 

#8 count()
def count8():
    a = l1.count(2)     # <list>.count(<value_to_count>)
    print(f"counted 2: {a}") 

count8()

# len for no of total characters and index to get index of specified value
# Appending and extending: append(), extend() for adding elements.
# Inserting and removing: insert(), pop(), remove() for modifying list contents.
# Sorting and reversing: sort(), reverse() for ordering.
# count for counting no of the same ele