# taking input
user_input = input("Greeting:" )
greeting = user_input.strip().lower()    #remove whitespace then convert to lower_case

# 3 cases for printing:
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
