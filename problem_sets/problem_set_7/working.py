import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    
    pattern = r"(\d{1,2})(:\d{2})? ([AP]M) to (\d{1,2})(:\d{2})? ([AP]M)"

    match = re.search(pattern, s)
    
    if not match:
        raise ValueError
    
    #Doing operations on both time frames one at a time:
    #First frame
    #Hour
    hour = int(match.group(1))
    if not (hour >=0 and hour <= 12):   #chk hour range is valid
        raise ValueError
    
    #minute
    minute = match.group(2)
    if minute:
        minute = minute[1:] # remove ':'
        if int(minute) >=60 or int(minute) <0 or len(minute) >2 : #check minute range is valid
            raise ValueError
    else:
        minute = "00"   # if no minute is mentioned

    #meridian
    meridian = match.group(3)
    #normal behaviour of time if hour is not 12
    if hour != 12:
        if meridian == "AM":
            new_hour = hour
        else:
            new_hour = hour + 12
    else:   # when the hour is 12
        if meridian == "AM":
            new_hour = 0
        else:
            new_hour = 12
    # adding the '0' str to formot 1 digit hours
    if new_hour <10:
        str_hour = f"0{new_hour}"
    else:
        str_hour = new_hour


    #2nd Time Frame
    #Hour
    hour = int(match.group(4))
    if not (hour >=0 and hour <= 12):   #chk hour range is valid
        raise ValueError
    
    #minute
    minute2 = match.group(5)
    if minute2:
        minute2 = minute2[1:] # remove ':'
        if int(minute2) >=60 or int(minute2) <0 or len(minute2) >2 : #check minute range is valid
            raise ValueError
    else:
        minute2 = "00"   # if no minute is mentioned

    #meridian
    meridian = match.group(6)
    #normal behaviour of time if hour is not 12
    if hour != 12:
        if meridian == "AM":
            new_hour = hour
        else:
            new_hour = hour + 12
    else:   # when the hour is 12
        if meridian == "AM":
            new_hour = 24
        else:
            new_hour = 12
    # adding the '0' str to formot 1 digit hours
    if new_hour <10:
        str_hour2 = f"0{new_hour}"
    else:
        str_hour2 = new_hour
        
    # End string
    return f"{str_hour}:{minute} to {str_hour2}:{minute2}"

if __name__ == "__main__":
    main()