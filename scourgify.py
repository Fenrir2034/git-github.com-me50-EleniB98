import csv
import sys

def main():
    # Ensure correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input_file.csv output_file.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            # Write header in the output file
            writer.writeheader()

            for row in reader:
                # Split name into first and last name
                last_name, first_name = row['name'].split(', ')
                # Write to output file
                writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})

        print("Conversion completed successfully.")
    except FileNotFoundError:
        sys.exit("Error: Input file not found.")

if __name__ == "__main__":
    main()




