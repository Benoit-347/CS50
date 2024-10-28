def main():
    a = []
    while True:
        a.append(my_fns.get_int("enter no: "))
        if input("continue: ") != "y":
            break
    print(avge(a))

import sys
sys.path.append("D:\My_Folder_Parent\Study\Programming\Python_files\CS50_harward_class\Class_4")
import my_fns
def avg(a):
    b = 0
    for i in a:
        b = b + i
    return b/len(a)

def avge(a):
    b = 0
    for i in a:
        i = i + i
    return b/len(a)

def hello(a = "world"):
    return "hello " + a


if __name__ == "__main__":
    main()
    