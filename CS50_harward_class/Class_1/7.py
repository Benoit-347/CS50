#match keyword available in recent versions of python(from 3.10)
a = input("enter name:")
match a:
    case "Benoit":
        print("semi pro")
    case "Danush":
        print("semi noob")
    case _:
        print("who?")

#or
match a:
    case "Benoit" | "Danush" | "Deekshith":
        print("friends")
    case _:
        print("who?")