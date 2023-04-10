import random

def main():
    level = get_level()
    problems = generate_problems(level)
    score = solve_problems(problems)
    print(f"Your score is {score}/10.")

def get_level():
    """
    Prompts the user for a level (1, 2, or 3) and returns it as an int.
    Re-prompts the user until a valid input is received.
    """
    level = 0
    while level not in [1, 2, 3]:
        try:
            level = int(input("Choose a level (1, 2, or 3): "))
        except ValueError:
            pass
    return level

def generate_problems(level):
    """
    Returns a list of 10 math problems formatted as X + Y =,
    where X and Y are non-negative integers with level digits.
    """
    problems = []
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y} = "
        problems.append(problem)
    return problems

def generate_integer(level):
    """
    Returns a randomly generated non-negative integer with level digits,
    or raises a ValueError if level is not 1, 2, or 3.
    """
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level.")

def solve_problems(problems):
    """
    Prompts the user to solve each problem in the list.
    Returns the number of correct answers.
    """
    score = 0
    for problem in problems:
        answer = None
        attempts = 0
        while answer != eval(problem[:-2]):
            if attempts == 3:
                print(f"The correct answer is {eval(problem[:-2])}.")
                break
            try:
                answer = int(input(problem))
            except ValueError:
                pass
            if answer != eval(problem[:-2]):
                print("Wrong!")
                attempts += 1
            else:
                score += 1
                print("Correct!")
    return score

if __name__ == "__main__":
    main()
