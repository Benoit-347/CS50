#using loops to get each element in file
def main1():
    a()
    b()
def a():
    with open("aa.txt", 'w') as file:
        file.write("hi\nhello\n\nbye\n")
def b():
    with open("aa.txt", 'r') as file:
        for i in file.readlines():
            print(i)
#main1()

#notice, the data is having a extra new line(when iterating, get element -> line (contains /n) -> the print() puts a new line in sideeffect)
#try print("a\nb\nc\n")

def c():
    with open("aa.txt", 'r') as file:
        for i in file.readlines():
            print(i.rstrip()) #removes whitespace only right of data -> when no data, does not remove

def main2():
    a()
    c()

main2()
 