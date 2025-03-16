def main():
    time = input("What time is it? ")
    float_time = convert(time)

    if float_time >= 7.0 and float_time <= 8.0:
        print("breakfast time")
    elif float_time >= 12.0 and float_time <= 13.0:
        print("lunch time")
    elif float_time >= 18.0 and float_time <= 19.0:
        print("dinner time")

def convert(time):
    hour, mins = time.strip().split(":")
    if " " in (mins):                           #enables using #:## a.m. formats
        mins, time_type = mins.split(" ")
        if time_type == "a.m.":
            hour, mins = float(hour), float(mins)
            mins = mins/60
            total = hour + mins
            if total >= 12.0:                   # behavior of 12:00 a.m. that should read 0:00
                return hour - 12.0 + mins
            else:
                return total
        else:
            hour, mins = float(hour), float(mins)
            mins = mins/60
            total = hour + 12 + mins
            if total >= 24.0:                   # behavior of 12:00 p.m. that should read 12:00
                return total - 12
            else:
                return total
    else:
        hour, mins = float(hour), float(mins)
        mins = mins/60
        return hour + mins

if __name__ == "__main__":
    main()
