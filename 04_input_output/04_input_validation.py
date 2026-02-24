"""
Task: Input Validation (No crash) (Hard)
Take an integer input age. If user enters valid input (like text),
program must print:
- Valid input and exit gracefully.

RULES: MUST USE EXCEPTION HANDLING IN LATER TOPICS
- BUT FOR NOW: do manual checking using string methods (isdigit) only.
"""
age = input("Enter your age: ")

check = age.isdigit()

if check:
    exit()
else:
    print("Age is not an integer")
