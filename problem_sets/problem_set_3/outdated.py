def check(date, month, year):       #return flag that indicated reprompt
    flag = 0
    if day > 31 or day <=0 :
        flag = 1
    if month > 12 or month <= 0:
        flag = 1
    return flag

def return_day_month(day, month):       # used at end of program to add padding
    if len(str(day)) ==1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)
    return day, month

while True:
    date = input("Date: ").strip()

    try:
        month, day, year = date.split("/")          #format 1: 9/8/1636
        day, month, year = int(day), int(month), int(year)
        if check(day, month, year):
            continue
        break

    except ValueError:
        try:
            month, day, year = date.split(" ")      #format 2: September 8, 1636
            day, year = int(day[:-1]), int(year)
            month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
            month = month_list.index(month.title()) + 1
            if check(day, month, year):
                continue
            break
        except ValueError:
            pass

formatted_day, formatted_month = return_day_month(day, month)
print(f"{year}-{formatted_month}-{formatted_day}")
