def convert(time_str):
    """
    Convert time in 24-hour or 12-hour format to the corresponding number of hours as a float.
    """
    if "a.m." in time_str or "p.m." in time_str:
        # 12-hour time format
        hours, minutes, period = time_str.split()[0].split(':')
        hours = int(hours) % 12
        if period == "p.m.":
            hours += 12
        return hours + int(minutes) / 60
    else:
        # 24-hour time format
        hours, minutes = map(int, time_str.split(':'))
        return hours + minutes / 60

def main():
    # Prompt user for time
    user_input = input("Enter the time in 24-hour or 12-hour format (HH:MM a.m./p.m.): ")

    # Convert user input to hours
    time_in_hours = convert(user_input)

    # Determine meal time
    if 7.0 <= time_in_hours < 12.0:
        print("breakfast time")
    elif 12.0 <= time_in_hours < 14.0:
        print("lunch time")
    elif 18.0 <= time_in_hours < 21.0:
        print("dinner time")

if __name__ == "__main__":
    main()
