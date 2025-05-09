def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length is between 2 and 6 characters
    if 2 <= len(s) <= 6:
        # Check if the first two characters are letters
        if s[:2].isalpha():
            # Check if the remaining characters are alphanumeric
            if s[2:].isalnum():
                # Check if the last character is a letter or a non-zero number
                if s[-1].isalpha() or (s[-1].isdigit() and s[-2] != '0'):
                    return True

    return False

main()



































