def main():         # this fn handles errors
    while True:

        input1 = input("Fraction: ").strip()

        try:
            print_output(input1)
            break
        except ZeroDivisionError:
            continue
        except ValueError:
            continue

def print_output(input1):
    x, y = input1.split("/")    # takes input and prints the neccesary output
    x = int(x)
    y = int(y)
    if x>y:
        raise ValueError
    percent = return_percent(x, y)
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(percent, "%", sep = "")

def return_percent(a,b):        # used to return a int with percentage value
    num = round(a/b*100)
    return num



main()
