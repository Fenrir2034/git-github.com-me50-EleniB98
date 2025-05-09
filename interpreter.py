def calculate_expression(x, operator, z):
    if operator == '+':
        return x + z
    elif operator == '-':
        return x - z
    elif operator == '*':
        return x * z
    elif operator == '/':
        return x / z

def main():
    # Prompt user for an arithmetic expression
    user_input = input("Enter an arithmetic expression (e.g., 1 + 1): ")

    # Split the input into x, operator, and z
    x, operator, z = user_input.split()

    # Convert x and z to integers
    x, z = int(x), int(z)

    # Calculate the result and print it formatted to one decimal place
    result = calculate_expression(x, operator, z)
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
    
