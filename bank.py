# program that prompts a user for a greeting
greeting = input("Please enter a greeting: ").strip().lower()

# checking the starting conditions of the user's greeting
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
