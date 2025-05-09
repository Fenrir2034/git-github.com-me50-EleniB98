def main():
    # Prompt user for input
    user_input = input("Please enter a string: ")

    # Split the input into words and join them with three periods
    modified_input = "...".join(user_input.split())

    # Print the modified input
    print(modified_input)

if __name__ == "__main__":
    main()
