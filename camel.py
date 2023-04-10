# we first define a function that converts camel to snake
def convert_to_snake(variable_name):
    snake_case = ''  # initialize empty string to take the snake version of variable name
    for i, char in enumerate(variable_name):  # iterate through each character in the variable name
        if i == 0:
            snake_case += char.lower()
        elif char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char

    return snake_case


variable_name = input("Please enter a variable name in camel case: ")
snake_case_name = convert_to_snake(variable_name)  # call the convert to snake function
print(f"The converted name to snake case is: {snake_case_name}")
