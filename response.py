# Install the validators library with: pip install validators
import validators

def validate_email(email):
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

def main():
    # Prompt the user for an email address
    user_email = input("Enter your email address: ")

    # Validate the email address
    validate_email(user_email)

if __name__ == "__main__":
    main()
