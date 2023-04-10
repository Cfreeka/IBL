text = input("Enter a text: ")  # prompt the user to enter a text

vowels = "aeiouAEIOU"  # define a string of vowels
no_vowels = ""  # empty string that will store the modified string with no vowels

for char in text:  # iterate through every character in the inputted text
    if char not in vowels:  # check if it is a vowel
        no_vowels += char  # append into the no_vowels empty string if it is not a vowel

print(f"Text with no vowels: {no_vowels}")  # print the modified text
