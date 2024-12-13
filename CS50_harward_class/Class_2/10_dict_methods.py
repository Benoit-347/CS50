dict1 = {'name': 'Alice', 'age': 20, 'subjects': ['Math', 'Physics']}

print("1. original dict:", dict1)
#method 1 <dict>.keys()
#Returns a list of all keys

to_print = dict1.keys()
print("2.", to_print)

#2: <dict>.values()
#returns a list of all values

print("3.", dict1.values())

#3: <dict>.items()
#returns a list of tuples containing key, value pairs

print("4.", dict1.items())

#4. get()
#Used to get values from key names from a dict, feature: can set default val (default set is None)
# Syn: <dict>.get(<key_name>, <default_return_value>)

print("5.", dict1.get('name'))
print("6.", dict1.get('class', 'B'))

#setdefault()
#used to get values from key names from a dict, feature: if key already does not exist, add key, value (you can set the default) to original dict
dict1.setdefault('height', 10)
print("7.", dict1.get('height'))