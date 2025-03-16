user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
answer = user_input.strip().lower()   #does not change original
result = "No"

# using match keyword
match answer:
    case "42" | "forty-two" | "forty two":      # Equivalent to "42" or "forty-two" or "forty two" :
        result = "Yes"

print(result)      #default is "No" changed to "Yes" only if matched
