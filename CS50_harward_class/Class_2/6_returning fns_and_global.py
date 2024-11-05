#how to use a function after defining it below code
def main():
    a = input("enter name")
    b = a*5
    hello(b) #when we suddenly want to define functions we want to do it in the latest line(bottom), but
             # to use it, it has to be defined above use, so we define main to structure flow and 
              # define fn at latest while still being useful

def hello(b):
    print("hello", b)
main()


#how to store value after function doing work?
#1 return, 2 global
def get_num():
    n = int(input("enter number:"))
    return n #temporaryly gives the value (next to return) when fn call is used a certain way

print(get_num())
#abstraction: potraying a idea(potentially complex) into language

#how to get number of elements in data? Can use for, but a performace optimized fn is len(<data>):
a = [5,6,4,7]
for i in range(len(a)): 
    print(a[i])