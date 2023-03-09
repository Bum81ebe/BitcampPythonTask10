# meal 2

def main():
    #asking for time
    question = input("What time is it? ")
    #convert time
    time = convert(question)
    # if else for specific times
    if time >= 7 and time <= 8:
        print("breakfast Time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    # split time to hours and minutes
    hours, minutes = time.split(":")
    # convert string to float
    time_convert = float(minutes) / 60
    return float(hours) + time_convert

if __name__ == "__main__":
    main()