import random

for _ in range(10):
    number_1 = random.randint(0,9)
    number_2 = random.randint(0,9)

    result = number_1 + number_2

    i = 0
    while True:
        i += 1
        if i == 4:
            print(f"{number_1} + {number_2} = {result}")
            break
        else:
            Input = int(input(f"{number_1} + {number_2} = "))
            if result != Input:
                print("EEE")
            else:
                break
