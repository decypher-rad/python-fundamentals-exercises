"""
Task 3 - Robust Input Parser (medium)

User enters input in this form:
name=George, age=26, height=178.5, working=yes

You must parse and output:
Name: George (str)
Age: 26 (int)
Height: 178.5 (float)
Working: True (bool)

Rules:
• You must not use external libraries
• Handle spaces properly (strip)
• Convert into correct types
• Convert yes/no into boolean
"""

name = input("Enter you first name: ")
age = int(input("enter your age: "))
height = float(input("enter your height: "))
working = input("Are you working? yes or no: ")
working_value = bool(working)

print(f"Name: {name} (str)")
print(f"Age: {age} (int)")
print(f"Height: {height} (float)")
print(f"Working: {working} (bool)")












