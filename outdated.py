from datetime import datetime

months = [
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

def main():
    while True:
        date_input = input("Enter a date (MM/DD/YYYY or Month Day, Year): ").strip()
        formatted_date = format_date(date_input)
        if formatted_date:
            print(formatted_date)
            break
        else:
            print("Invalid date. Please try again.")

def format_date(date_input):
    try:
        # Attempt to parse input as MM/DD/YYYY format
        date_obj = datetime.strptime(date_input, "%m/%d/%Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        try:
            # Attempt to parse input as Month Day, Year format
            for i, month in enumerate(months, start=1):
                if month.lower() in date_input.lower():
                    date_input = date_input.replace(month.lower(), str(i))
                    date_obj = datetime.strptime(date_input, "%m %d, %Y")
                    return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            return None

if __name__ == "__main__":
    main()
