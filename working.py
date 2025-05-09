import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'^(\d{1,2}):(\d{2}) (AM|PM) to (\d{1,2}):(\d{2}) (AM|PM)$'
    match = re.match(pattern, s)
    if match:
        start_hour = int(match.group(1))
        start_minute = int(match.group(2))
        start_meridiem = match.group(3)
        end_hour = int(match.group(4))
        end_minute = int(match.group(5))
        end_meridiem = match.group(6)

        if start_hour == 12:
            start_hour = 0
        if end_hour == 12:
            end_hour = 0

        if start_meridiem == 'PM':
            start_hour += 12
        if end_meridiem == 'PM':
            end_hour += 12

        if not (0 <= start_hour <= 23 and 0 <= end_hour <= 23 and
                0 <= start_minute <= 59 and 0 <= end_minute <= 59):
            raise ValueError("Invalid time")

        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
    else:
        raise ValueError("Invalid format")


if __name__ == "__main__":
    main()
