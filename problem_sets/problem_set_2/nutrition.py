fruit = input("Input: ").lower()

def print_cal(num):
    print("Calories:", num)

def using_match(fruit):     # method 1: using match for each fruit
    match fruit:
        case "apple":
            print_cal(130)
        case "avocado":
            print_cal(50)
        case "banana":
            print_cal(110)
        case "cantaloupe":
            print_cal(50)
        case "grapefruit":
            print_cal(60)
        case "grapes":
            print_cal(90)
        case "honeydew melon":
            print_cal(50)
        case "kiwifruit":
            print_cal(90)
        case "lemon":
            print_cal(15)
        case "lime":
            print_cal(20)
        case "nectarine":
            print_cal(60)
        case "orange":
            print_cal(80)
        case "peach":
            print_cal(60)
        case "pear":
            print_cal(100)
        case "pineapple":
            print_cal(50)
        case "plums":
            print_cal(70)
        case "strawberries":
            print_cal(50)
        case "sweet cherries":
            print_cal(100)
        case "tangerine":
            print_cal(50)
        case "watermelon":
            print_cal(80)

def using_dict(fruit):      #method 2: using dict as provided in hint
    dict1 = {
            "apple":130,
            "avocado":50,
            "banana":110,
            "cantaloupe":50,
            "grapefruit":60,
            "grapes":90,
            "honeydew melon":50,
            "kiwifruit":90,
            "lemon":15,
            "lime":20,
            "nectarine":60,
            "orange":80,
            "peach":60,
            "pear":100,
            "pineapple":50,
            "plums":70,
            "strawberries":50,
            "sweet cherries":100,
             "tangerine":50,
             "watermelon":80
    }
    if fruit in dict1:
        print_cal(dict1[fruit])

using_dict(fruit)
