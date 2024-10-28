def readfull_content():
    with open("aa.txt", 'r') as file2:
        print(file2.readlines())
def a():
    a = ""  #if list, the brackets would be input as it is into txt
    for _ in range(3):
        b = input("enter str: ") + "\n" #\n when in str still acts as finish line
        a = a + b 
    with open("aa.txt", 'w') as file:
        file.write(f"{a}\n") 
    readfull_content()
a()