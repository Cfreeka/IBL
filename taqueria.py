# Define the menu dictionary with items and prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


# Create an empty list to store the user's order
user_order = []


# Initialize the total cost to zero
total_cost = 0


# Loop until the user inputs control-d to end the program
while True:
    try:
        # Prompt the user to enter an item and titlecase it for case insensitivity
        item = input("Enter an item: ").title()

        # Look up the price of the item in the menu dictionary
        price = menu.get(item)

        # If the item is in the menu, add it to the order and update the total cost
        if price:
            user_order.append(item)
            total_cost += price
            print(f"Total cost: ${total_cost:.2f}")

    # Catch the EOFError that occurs when the user inputs control-d to end the program
    except EOFError:
        break
