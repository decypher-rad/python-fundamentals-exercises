"""
Task 2: Number properties (medium)
Input: one integer n
Output should print:
	•	Is it divisible by 2?
	•	Is it divisible by 3?
	•	Is it divisible by 5?
	•	Is it between 1 and 100 (inclusive)?

Rules:
	•	Must use %, and, or
	•	Output must be True/False
"""

n = int(input("Enter the value of n: "))

if n % 2 == 0:
    print(f"True {n} is divisible by 2")
else:
    print(f"False {n} is not divisible by 2")

if n % 3 == 0:
    print(f"True {n} is divisible by 3")
else:
    print(f"False {n} is not divisible by 3")

if n % 5 == 0:
    print(f"True {n} is divisible by 5")
else:
    print(f"False {n} is not divisible by 5")

if 1 <= n <= 100:
    print(f"{n} is between 1 and 100")
