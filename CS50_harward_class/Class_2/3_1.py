#references
#mtuable, on normal assgnment only shares ref id (values not copied)
l1 = [1,2,3,4,5]
l2 = l1
l2.pop()
print(f"1. popped list: {l2}, original list: {l1}")
print(f"id of l1 is: {id(l1)}, id of l2 is: {id(l2)}")

#on copy() fn does shallow copy (copies only parent values) snd the nested values ref ids are copied.
#parent change
l1 = [1,2,3,4,5,[10, 20]]
l2 = l1.copy()
l2.pop(5)
print(f"2. popped list: {l2}, original list: {l1}")
print(f"id of l1 is: {id(l1)}, id of l2 is: {id(l2)}")

#nested list value change
l1 = [1,2,3,4,5,[10, 20]]
l2 = l1.copy()
l2[5].pop(1)
print(f"3. popped list: {l2}, original list: {l1}")
print(f"id of l1[5] is: {id(l1[5])}, id of l2[5] is: {id(l2[5])}")

#copying all values from a list (deep copy), by importing method
import copy
l1 = [1,2,3,4,5,[10, 20]]
l2 = copy.deepcopy(l1)
l2[5].pop(1)
print(f"4. popped list: {l2}, original list: {l1}")
print(f"id of l1[5] is: {id(l1[5])}, id of l2[5] is: {id(l2[5])}")
