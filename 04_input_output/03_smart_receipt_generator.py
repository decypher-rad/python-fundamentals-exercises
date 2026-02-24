"""
Task 3 - Smart Receipt Generator (Hard)
Input:
- Item1 price
- Item2 price
- Item3 price
- tax %
- discount %

Output format receipt like:
Subtotal : £xxx.xx
Tax      : £xx.xx
Discount : -£xx.xx
Total    : £xxx.xx

Rules: must be aligned nicely (like receipt).
"""
Item1 = float(input("Item 1 price: "))
Item2 = float(input("Item 2 price: "))
Item3 = float(input("Item 3 price: "))

tax_percent = float(input("Enter the tax %: "))
discount_percent = float(input("Enter the discount %: "))

total = Item1 + Item2 + Item3
tax = (total * tax_percent)/100
after_tax = total + tax
discount = (after_tax * discount_percent)/100

final_bill = after_tax - discount

print("=" * 25)
print(f"Subtotal  : £{total}")
print(f"Tax       : £{tax}")
print(f"Discount  : -£{discount}")
print(f"Total     : £{final_bill}")
print("=" * 25)
