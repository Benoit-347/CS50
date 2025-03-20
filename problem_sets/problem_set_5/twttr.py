def main():
    word = input("Input: ")
    result = shorten(word)
    print(result)

def shorten(word):
    result = ""
    for i in word:
        if i in "AEIOUaeiou":       # checks for lower and upper case
            continue
        result = result + i
    return result


if __name__ == "__main__":
    main()
