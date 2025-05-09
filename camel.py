def camel_to_snake(camel_case):
    """
    Convert a variable name from camel case to snake case.
    """
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    # Remove leading underscore, if any
    return snake_case.lstrip("_")

def main():
    # Prompt user for variable name in camel case
    camel_case_input = input("Enter the variable name in camel case: ")

    # Convert to snake case and print the result
    snake_case_output = camel_to_snake(camel_case_input)
    print(snake_case_output)

if __name__ == "__main__":
    main()
