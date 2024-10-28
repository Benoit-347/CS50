#problem set 0
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(a):
    a = a.replace("$", "")
    a = float(a)
    return a
def percent_to_float(b):
    b = b.replace("%", "")
    b = float(b)/100
    return b
main()