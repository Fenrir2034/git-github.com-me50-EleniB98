from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    """Main Function"""
    birthdate = get_date(input("Your Birthdate (YYYY-MM-DD): "))
    total_minutes = calculate_minutes_elapsed(birthdate)
    print(convert_to_song_format(total_minutes))

def get_date(user_input):
    """
    (str) -> (date)

    Get the date and ensure it is typed
    in the correct format
    """
    try:
        # Convert input to datetime.date() class
        birthdate = date(*map(int, user_input.split('-')))
    except (ValueError, IndexError):
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")

    return birthdate

def calculate_minutes_elapsed(birthdate):
    """(date) -> (int)"""
    current_date = date.today()
    difference = (current_date - birthdate).total_seconds()
    return int(difference / 60)

def convert_to_song_format(minutes):
    """(int) -> (str)"""
    words = p.number_to_words(minutes)
    return words.replace(" and", "").capitalize() + " minutes"

if __name__ == "__main__":
    main()

