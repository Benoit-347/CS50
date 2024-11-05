#advanced version of elif, useful when different values should give same output (multiple or's)

#match keyword available in recent versions of python(from 3.10)
#used as conditionals

#syn:
#match <value to compare from>:
#    case <vakue to compare to> | <another value to compare to> | <...infinite such arg>:
#        <work>

a = "idk"
match a:
    case "Benoit" | "Danush" | "Deekshith"|"idk":
        print("friends")
    case "idk":
        print("even idk")
    case _:
        print("who?")

#like
a = "idk"
if a == "Benoit" or a == "Danush" or a == "Deekshith" or a == "idk":
    print("friends")
elif a == "idk":
    print("even idk")
else:
    print("who?")