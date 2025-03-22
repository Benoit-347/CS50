import sys

def main():
    # taking input
    user_input = input("Greeting:" )
    print(f"${value(user_input)}")


def value(greeting):

    # taking input
    greeting = greeting.strip().lower()    #remove whitespace then convert to lower_case

    # 3 cases for returning:
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
