def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (len(s)>=2 and len(s)<=6):   # 2 to 6 characters
        return False
    if not s[:2].isalpha():        # at least 2 letters
        return False

    flag = 0
    for i in s:

        if flag ==0 :           # when encountring 1st number
            if i.isdigit():
                if i =="0":
                    return False
                flag = 1

        if flag ==1:        # after a number was encountered
            if i.isalpha():
                return False

        if not i.isalnum(): # only allows alphabets or numbers
            return False

    return True



if __name__ == "__main__":
    main()
