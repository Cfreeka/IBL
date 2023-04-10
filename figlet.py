import sys
import random
import pyfiglet

# Define the available fonts
fonts = pyfiglet.FigletFont.getFonts()

# Parse command-line arguments
if len(sys.argv) == 1:
    # No arguments provided, use a random font
    font_name = random.choice(fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in fonts:
    # Two arguments provided and the first is "-f" or "--font" and the second is a valid font name
    font_name = sys.argv[2]
else:
    # Invalid arguments provided
    print("Usage: python figlet.py [-f FONT] [TEXT]")
    print("Available fonts:")
    print(", ".join(fonts))
    sys.exit(1)

# Prompt the user for input text
text = input("Enter some text to be displayed in FIGlet font: ")

# Create a FIGlet object with the desired font
figlet = pyfiglet.Figlet(font=font_name)

# Output the text in the desired font
print(figlet.renderText(text))
