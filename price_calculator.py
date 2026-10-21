
# Python Week 1 Assignment
# This program calculates the total cost of items.

# Ask the user to enter the price and quantity
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity you want: "))

# Calculate the total cost
total = price * quantity

# Display a friendly summary using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
