#0 str operations

a = "hi"
b = a + "bye" #concatenation
c = a*3 #replication
print(b,c)

#1. strip
#removes specified characters at beggining or end
a = "\nhi hello   \n\n"
a = a.strip("h")
a = a.rstrip()

#2. capitalize
a = "hi bro a b c"
a = a.capitalize()
#Capitalize first character of str

#3 title
#capitalize first character of every word
a = "hi bro a b c"
a = a.title()
print(a)


#4 split
#used to convert the str to multiple str at specified character
a = "hello world"
a = a.split()
#default is space
#makes multiple strings (depending on how many characters match split agrument) by default stored as list
print(a)

a, b,c = a.split("o")
# split thrice 
#removes the character where split occured
print(a,b,c)
#need to convert string to another character

#5 replace
#to convert a particular value in string to another character
#no remove fn in str, use replace
a = "hi bro A b c"
a.replace("A", "benoit")
print(a)