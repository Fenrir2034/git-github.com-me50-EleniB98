def get_fraction():
    while True:
        try:
            fraction_str = input("Enter a fraction in the format X/Y: ")
            numerator, denominator = map(int, fraction_str.split('/'))

            if denominator == 0 or numerator > denominator:
                raise ValueError("Invalid fraction. Please try again.")

            return numerator, denominator

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError:
            print("Error: Denominator cannot be zero.")

def calculate_percentage(numerator, denominator):
    percentage = (numerator / denominator) * 100
    return round(percentage)

def main():
    while True:
        try:
            numerator, denominator = get_fraction()

            if numerator == denominator:
                print("F")
            elif numerator / denominator <= 0.01:
                print("E")
            elif numerator / denominator >= 0.99:
                print("F")
            else:
                percentage = calculate_percentage(numerator, denominator)
                print(f"{percentage}%")
            break

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError:
            print("Error: Denominator cannot be zero.")

if __name__ == "__main__":
    main()

