# Initialize an empty dictionary to keep track of the user's input
grocery_list = {}

# Prompt the user for input
try:
    while True:
        item = input("Enter an item for your grocery list (press ctrl-d when finished): ")
        # Convert the item to uppercase and add it to the dictionary
        item = item.upper()
        grocery_list[item] = grocery_list.get(item, 0) + 1
except EOFError:
    # User has finished entering items
    pass

# Sort the dictionary by key and output the results
for item in sorted(grocery_list):
    # Get the count for this item
    count = grocery_list[item]
    # Output the count and item name in the desired format
    print(f"{count} {item}")
