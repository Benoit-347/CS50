#how to sort a list of dicts wrt to a specific key of dict?
def a(dict):
    return dict["name"]
#made temp dict to show what key to check for (to show check "name")

list1 = [{"name":30, "value":100}, {"name":20, "value":200}, {"name":10, "value":300}]
for i in sorted(list1, key=a):
    print(i)

#sorts the dicts in list according to value associated with key "name"
# the a() fn req to show sorted how to obtain the value (to sort wrt)

#iterations not the part of syn; do not req 'for' loop
print(sorted(list1, key=a))
print("2. ", end = "")


#part 2


#we do not req to use the above fn a() as we only req it during sorting and later never touched. So instead of creating reusable fn, you can create a 1 time fn using lambda
print(sorted(list1, key=lambda dict: dict["name"])) # lambda <parameter>: <return>
# pass the parameter variable name, then the texr after semi colon return that value

#(no def statement) and did not pass fn name  (creates a fn on spot and calls it so no neeed)


#part 3


#lamda is used to create a quick fn as well (by passing it to a var)

square = lambda var1: var1**2
print(square(2))

#can make small code by combining with list comprehentions
#ONly use case: Make single line fns (easy making) so used in guis and libraries