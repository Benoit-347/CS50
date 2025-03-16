word = input("Input: ")
result = ""
for i in word:
    if i in "AEIOUaeiou":       # checks for lower and upper case
        continue
    result = result + i
print("Output:", result)
