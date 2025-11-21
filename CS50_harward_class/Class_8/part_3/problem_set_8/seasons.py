from datetime import date
import sys

def str_to_date(string):
    date_list = string.split('-')
    int_list = [int(i) for i in date_list]
    date_birthday = date(int_list[0], int_list[1], int_list[2])
    return date_birthday

def get_mins(date_now, date_birthday):
    num_days = date_now - date_birthday
    num_seconds  = num_days.total_seconds()
    return int(num_seconds/60)

def get_prefix(number = 999):
    units = ["","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen",
            "sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    output = ""
    if number // 100:
        output =  units[number//100] + ' hundred'
        number = number - (number //100)*100

    if number %100:
        if number >=20:
            output = ' '.join([output, tens[number //10]]).strip()
            if number %10 and number //1:
                output = output + '-' + units[number%10]
                return output
        elif number >9:
            output = ' '.join([output, teens[number-10]]).strip()
            return output
        
    if number %10 and number //1:
        output = ' '.join([output, units[number%10]]).strip()

    return output

def conv_num_to_str(number):
    thousands = ["","thousand","million","billion"]
    place = 0
    output = ''
    
    while number/1000:
        output =  get_prefix(number %1000) + ' ' + thousands[place] + output
        number //= 1000
        place +=1
        if number:
            output = ', ' + output

    return output.capitalize().strip()

def main():
    user_in = input("Date of Birth: ")
    if user_in.count('-') != 2:
        print("Invalid date")
        sys.exit(1)
    else:
        date_birthday = str_to_date(user_in)
        date_now = date.today()
        minutes = get_mins(date_now, date_birthday)

        print(conv_num_to_str(minutes) + ' minutes')

if __name__ == "__main__":
    main()
