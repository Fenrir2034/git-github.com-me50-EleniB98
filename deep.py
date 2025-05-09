def Great_Question():
    # Prompt for user for the answer to the Great Question
    user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # The user input must be 42, forty-two, or forty two
    if user_input.strip().lower() in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    Great_Question()
