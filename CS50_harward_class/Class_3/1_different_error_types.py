#Explain what different errors mean:

#SyntaxError: eorror in the format of code
def syntax_error():
    try:            
        print("hi)      #cannot catch hard coded syn errors can this stops runtime immediately
    except SyntaxError:
        print("syntax_error")
          
#ValueError: invalid argument/ datatype
def Value_Error_1():
    print(int("hello"))

#NameError: Variable name error(usually not defined)
def Name_Error_1():
    try:
        a = int(input("enter charac"))  #may have ValueErrror
    except:
        pass
    print(a)    #may have NameErrror

#AttributeError
#NameError
#RuntimeError	Raised when an error does not fall under any other category.