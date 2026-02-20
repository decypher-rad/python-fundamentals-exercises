"""
Task 2 - Type conversion challenge (medium)
Take input:
  - Salary as a string
  - Bonus percent as string
Convert both and calculate:
  - Bonus amount
  - Total salary after bonus
"""

salary = input("Enter the total salary amount: ")
bonus_percent = input("Enter the Bonus percentage: ")

salary = float(salary)
bonus_percent = float(bonus_percent)

bonus = (salary * bonus_percent)/100
Total = salary + bonus
print(f"Bonus = {bonus}")
print(f"Total = {salary}")
