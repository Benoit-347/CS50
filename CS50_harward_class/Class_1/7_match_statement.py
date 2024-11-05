#match keyword available in recent versions of python(from 3.10)
#advanced version of elif, useful when different values should give same output (multiple or's)

a = input("enter name:")
match a:
    case "Benoit":
        print("semi pro")
    case "Danush":
        print("semi noob")
    case _:
        print("who?")

#or

#syn:
#match <value to compare from>:
#    case <vakue to compare to> | <another value to compare to> | <...infinite such arg>:
#        <work>

match a:
    case "Benoit" | "Danush" | "Deekshith":
        print("friends")
    case "idk":
        print("even idk")
    case _:
        print("who?")