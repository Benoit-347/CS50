#print takes infinite arguments

#by default when print is used a character of new line is also input gives a next line data command
print("printed1")

print("printed2", end = '')
#use end = (inside quote) to specify the data to produce after sideeffect is shown
print("printed3")

print("hi","bye", sep = "a")
#sep is default " ", it is executed only when multiple side effects are printed(seperated by the commas)
#sep value has to be a string or none(no list, tuple or string

#can you assign values in arguments in py?
try:
    print(s = 2 )
except:
    print("it takes assignment with = as keyword argument")

#To assign while printing, use a feature from python 3.8 onwards
s = 1
print(s:= 2)
print(s)
#try:
#    print("hi", "bye", sep = ""a"")
#double beginning quotes give error as it translates to a beggining and ending
#use escape characters to show the squence of tasks
print("hi", "bye", sep = "\"a\"")
#2nd escape character continues after next character


#how does print get new line? When print encounters \n -> side effect finishes current line
print("a\nb")