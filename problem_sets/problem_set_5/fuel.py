def main():
    while True:
        input1 = input("Fraction: ").strip()
        try:
            percentage = convert(input1)
            percent_str = gauge(percentage)
            print(percent_str)
            break
        except ZeroDivisionError:
            continue
        except ValueError:
            continue

#to return a percent of x/y in 100

def convert(fraction):
    try:
        x, y = fraction.split("/")    # Split on "/"
    except:
        raise ValueError

    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
    else:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError
    percentage = round(x / y * 100)
    return percentage

# return a string of percent with added E and F when neccesary
def gauge(percentage):
    if 100 < percentage or percentage < 0:
        raise ValueError
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
