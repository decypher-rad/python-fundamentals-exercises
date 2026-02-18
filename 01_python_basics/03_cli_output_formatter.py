"""
Task 3 - CLI Output Formatter (hard)
Write a program that prints a dynamic boxed output like below:
+---------------------+
|  Python is awesome!  |
+---------------------+
"""

text = input("Enter a sentence: ")

print("+" + ("-" * len(text)) + "+")
print("|" + text + "|")
print("+" + ("-" * len(text)) + "+")
