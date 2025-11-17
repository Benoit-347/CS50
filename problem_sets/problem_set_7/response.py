import validators

user_input = input("What's your email address?").strip()

validate = validators.email(user_input)

if validate:
    print("Valid")
else:
    print("Invalid")
