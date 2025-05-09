def convert(input_str):
    """
    Convert :) to 🙂 and :( to 🙁 in the input string.
    All other text is returned unchanged.
    """
    converted_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_str

def main():
    # Prompt user for input
    user_input = input("Please enter a string: ")

    # Call convert function and print the result
    result = convert(user_input)
    print(result)

if __name__ == "__main__":
    main()
