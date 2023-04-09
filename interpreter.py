# A prompt asking the user to input an arithmetic expression
expression = input("Enter an arithmetic expression: ")
x, y, z = expression.split()

# define the integer variables x and z
x = int(x)
z = int(z)

# conditional statements checking what kind of operator is being used in the expression
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    print("Invalid operator")
    exit()

print("{:.1f}".format(result))
