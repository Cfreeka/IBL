amount_inserted = 0  # keeps track of total amount the user has inserted

while amount_inserted < 50:  # ensures the program runs as long as amount is less than 50
    coin = int(input("Please insert a coin (25, 10, or 5 cents): "))  # accepts integers as user inputs
    if coin == 25 or coin == 10 or coin == 5:
        amount_inserted += coin
        break
    else:  # ignores an integer than isn't an accepted denomination
        print("Invalid coin. Please insert a 25, 10, or 5 cent coin.")

change = amount_inserted - 50

if change > 0:
    print("You are owed", change, "cents.")
else:
    print("Thank you. Enjoy your Coke!")
