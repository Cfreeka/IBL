while True:  # prompt the user till we receive a valid input
    """use try and except blocks to catch any exceptions"""
    try:
        fraction = input("Please enter the fuel gauge fraction (in the format X/Y): ")
        x, y = map(int, fraction.split('/'))
        if x <= 0 or y <= 0 or x > y:
            raise ValueError
        break  # break out of the loop if we have valid values of x and y
    except ValueError:
        print("Invalid input. Enter two positive integers separated by a slash (e.g. 1/5).")
    except ZeroDivisionError:
        print("Invalid input. Y cannot be zero.")

percentage = round((x / y) * 100)  # compute the percentage then we round it to the nearest integer

if percentage <= 1:  # check if it is empty or full
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
