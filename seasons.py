import sys
from datetime import date


def main():
    # Prompts user for their date of birth in the format YYYY-MM-DD
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

    # Try to parse the input string as a date
    # Ensures no exceptions are raised
    try:
        dob = date.fromisoformat(dob_str)
    except ValueError:
        # If input is not in the correct format, exit with an error message
        print("Error: invalid date format (should be YYYY-MM-DD)")
        sys.exit(1)

    # Calculate the user's age in minutes, assuming they were born at midnight on their birthdate
    now = date.today()
    age_in_minutes = round((now - dob).total_seconds() / 60)

    # Convert the age in minutes to English words, using the Rent song format
    hours, minutes = divmod(age_in_minutes, 60)
    days, hours = divmod(hours, 24)
    months, days = divmod(days, 30)
    years, months = divmod(months, 12)

    age_str = ""
    if years > 0:
        age_str += f"{years} year"
        if years > 1:
            age_str += "s"
    if months > 0:
        if years > 0:
            age_str += ", "
        age_str += f"{months} month"
        if months > 1:
            age_str += "s"
    if days > 0:
        if years > 0 or months > 0:
            age_str += ", "
        age_str += f"{days} day"
        if days > 1:
            age_str += "s"
    if hours > 0:
        if years > 0 or months > 0 or days > 0:
            age_str += ", "
        age_str += f"{hours} hour"
        if hours > 1:
            age_str += "s"
    if minutes > 0:
        if years > 0 or months > 0 or days > 0 or hours > 0:
            age_str += ", "
        age_str += f"{minutes} minute"
        if minutes > 1:
            age_str += "s"

    # Sing the result!
    print("Happy happy birthday to you, dear user!")
    print(f"You are {age_str} old!")
    print("Happy birthday to you!")


if __name__ == "__main__":
    main()
