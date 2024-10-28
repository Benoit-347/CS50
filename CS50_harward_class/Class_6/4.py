#return a list after sorting (not sort original list)
def main_create():
    with open('aa.txt', 'w') as file:
        file.write("benoit\nDanush\nDeekshit\n")
def main_raw():
    a = []
    with open("aa.txt", 'r') as file:
        for i in file.readlines():
            a.append(i)
    print(a)

def main_stripped_sorted():
    a = []
    with open("aa.txt", 'r') as file:
        for i in file.readlines():
            a.append(i.rstrip())
    for i in sorted(a):
        print(i)

def main():
    main_create()
    main_raw()
    main_stripped_sorted()

main()