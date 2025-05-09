# Define a dictionary with fruit names and their corresponding calories
fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "sweet cherries": 100,
    "kiwifruit": 90,
    "pear": 100
}

# Prompt user for input
user_input = input("Enter a fruit: ")

# Convert user input to lowercase and remove leading/trailing spaces for case-insensitive matching
user_input_lower = user_input.lower().strip()

# Check if the entered fruit is in the dictionary
if user_input_lower in fruit_calories:
    # Output the calories for the entered fruit
    print(f"Calories: {fruit_calories[user_input_lower]}")
else:
    # Ignore input that isn't a fruit
    pass

