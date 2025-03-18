import random

def get_int(msg):   #takes int input else retry
    while True:
        try:
            Input = int(input(msg))
            break
        except:
            pass
    return Input

n = get_int("Level: ")
The_number = random.randint(0,n)    #generate random int from 0 to n (inclusive of both)

while True:
    guess = get_int("Guess: ")

    if guess == The_number:         #continues asking guess until correct
        print("Just right!")
        break
    elif guess > The_number:
        print("Too large!")
    else:
        print("Too small!")
