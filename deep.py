"""Prompts the user for an answer"""
user_answer = input(
    "What is the answer to the Great Question of life, the Universe and Everything?  ")

'''Condition checking the user input and case-insensitiveness of the answer'''
if user_answer.strip().lower() in ['42', 'forty-two', 'forty two']:
    print("Yes")
else:
    print("No")
