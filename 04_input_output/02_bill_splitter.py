"""
Task 2: Bill splitter (medium)
Input:
- total bill amount
- number of people
- tip percentage

Output:
- tip amount
- total with tip
- per person amount

Rules: use float division, format to 2 decimals
"""

total = float(input("enter the total bill amount: "))
num_of_people = int(input("enter the total number of people: "))
tip = float(input("enter the tip percentage: "))

tip_amount = (total * tip)/100
bill = total + tip_amount
amount = bill/num_of_people
final_amount = (amount * 100) // 1 / 100

print(f"The total bill amount is {total}")
print(f"The total bill with tip is {bill}")
print(f"Amount per person is {final_amount}")
