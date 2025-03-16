user_input = input("camelCase: ").strip()
result = ""


for char in user_input:
    if char.isupper():      # An uppercase denotes new word
        result = result + "_" + char.lower()
    else:
        result = result + char

print(result)
