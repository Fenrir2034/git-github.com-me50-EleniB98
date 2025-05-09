menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def calculate_total(order_items):
    total = sum(menu[item] for item in order_items)
    return total

def main():
    order_items = []

    try:
        while True:
            item_input = input("Enter an item: ")

            # Check if the input is in the menu and case-insensitive
            item = next((menu_item for menu_item in menu if menu_item.lower() == item_input.lower()), None)

            if item:
                order_items.append(item)
                total = calculate_total(order_items)
                print(f"Total: ${total:.2f}")
            else:
                print("Invalid item. Please enter a valid item from the menu.")

    except EOFError:
        # Handle end of input (control-d)
        total = calculate_total(order_items)
        print(f"Final Total: ${total:.2f}")

if __name__ == "__main__":
    main()
