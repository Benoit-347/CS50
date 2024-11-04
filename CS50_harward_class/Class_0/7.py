#to store strings after split
a = input("enter").strip().title()
print(a)
a = a.split()
#default is space
#makes multiple strings (depending on how many characters match split agrument) so default stored as list
print(a)
a = "hello world"
a, b,c = a.split("o")
#2 o, split thrice 
#removes the character where spit occured
print(a)
print(b)
print(c)


#need to convert string to another character
#no remove fn in str, use replace
a.replace("A", "benoit") #value initial, final
print(a)