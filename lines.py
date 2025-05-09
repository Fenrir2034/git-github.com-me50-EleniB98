import sys

def count_lines_of_code(file_name):
    try:
        with open(file_name, 'r') as file:
            count = 0
            for line in file:
                if not line.lstrip().startswith("#") and line.strip() != "":
                    count += 1
        return count
    except FileNotFoundError:
        raise FileNotFoundError

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")
    file_name = sys.argv[1]
    # Verify if the provided file name ends with ".py"
    if not file_name.endswith('.py'):
        sys.exit("Not a Python file")
    # Count lines of code
    try:
        lines_of_code = count_lines_of_code(file_name)
        print(lines_of_code)  # Only print the count of lines of code
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()





