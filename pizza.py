import sys
import csv
from tabulate import tabulate

def print_pizza_table(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            pizza_data = list(reader)
            print(tabulate(pizza_data, headers='firstrow', tablefmt='grid'))
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_name = sys.argv[1]
    # Verify if the provided file name ends with ".csv"
    if not file_name.endswith('.csv'):
        sys.exit("Not a CSV file")

    # Print the pizza table
    print_pizza_table(file_name)

if __name__ == "__main__":
    main()
