def bank_program():
    # Prompt user for a greeting
    user_greeting = input("Please enter a greeting: ")

    # Remove leading whitespace and make the greeting case-insensitive
    user_greeting_stripped = user_greeting.strip().lower()

    # Check conditions and output the corresponding amount
    if user_greeting_stripped.startswith("hello"):
        print("$0")
    elif user_greeting_stripped.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    bank_program()
