import random


def main():             #to print addition question allowing 3 tries and prints resulting score
    n = get_level()
    score = 0       # stores score
    for _ in range(10):     # 10 questions
        i = 0
        x = generate_integer(n)
        y = generate_integer(n)
        result = x + y
        while True:     # to allow 3 re tries
            i += 1
            if i == 4:
                print(f"{x} + {y} = {result}")
                break
            Input = int(input(f"{x} + {y} = "))
            if result == Input:
                score += 1
                break
            else:
                print("EEE")
    print(f"Score: {score}")

def get_level():    # used to denote num of digits in question, generated
    while True:

        try:
            n =  int(input("Level: "))
            match n:
                case 1|2|3:
                    break
                case _:
                    raise ValueError
        except ValueError:
            continue

    return n

def generate_integer(level):    # produces a random int with level-digits
    if level == 1:
        x = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
    elif level ==3:
        x = random.randint(100, 999)
    return x

if __name__ == "__main__":
    main()
