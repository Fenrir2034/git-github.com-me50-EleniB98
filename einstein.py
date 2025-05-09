def einstein():
    # Prompt user for mass in kilograms
    mass = int(input("Please enter the mass in kilograms: "))

    # Calculate energy using the famous equation E=mc^2
    energy = mass * (3 * 10**8)**2

    # Print the result
    print(energy)

if __name__ == "__main__":
    einstein()
