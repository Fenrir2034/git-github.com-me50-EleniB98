from collections import Counter

def main():
    grocery_list = read_grocery_list()
    display_grocery_list(grocery_list)

def read_grocery_list():
    grocery_items = []
    try:
        while True:
            item = input().strip().lower()
            grocery_items.append(item)
    except EOFError:
        pass  # End of input with control-d

    return grocery_items

def display_grocery_list(grocery_list):
    # Count occurrences of each item
    item_counts = Counter(grocery_list)

    # Sort items alphabetically
    sorted_items = sorted(item_counts.items())

    # Display the grocery list
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
