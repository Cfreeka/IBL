# Import email validation function from validators module
from validator_collection import validators

# Prompt user to enter an email address which is then stored in a variable called email
email = input("Enter an email address: ")

# Call the email validation function from the validators module on the 'email' variable
if validators.email(email):
    # If email is valid, print "Valid"
    print("Valid")
else:
    # If email is not valid, print "Invalid"
    print("Invalid")
