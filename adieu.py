# Create an empty list to store the names entered by the user
names = []

# Loop until the user inputs control-d
while True:
    try:
        # Prompt the user to enter a name
        name = input("Enter a name: ")
    except EOFError:
        # If the user inputs control-d, exit the loop
        break
    # Add the name to the list of names
    names.append(name)

# Check the length of the list of names
if len(names) == 1:
    # If there is only one name, print a simple farewell message
    print("Adieu, adieu, to", names[0])
else:
    # If there are multiple names, construct a farewell message
    farewell = "Adieu, adieu, to "
    for i, name in enumerate(names):
        if i == len(names) - 1:
            # If this is the last name, add "and" before the name
            farewell += "and " + name
        elif i == len(names) - 2:
            # If this is the second-to-last name, add a space before the name
            farewell += name + " "
        else:
            # If this is not the last or second-to-last name, add a comma and a space after the name
            farewell += name + ", "
    # Print the farewell message
    print(farewell)
