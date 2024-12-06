price_childrens = float(input("What is the price of a child's meal? "))
price_adults = float(input("What is the price of an adult's meal? "))
sunday = float(input("What is the price of a chocolate fudge sunday? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
sundays = int(input("How many chocolate fudge sundays were there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

subtotal = (price_childrens * children) + (price_adults * adults) + (sunday * sundays)
print(f"\nSubtotal: ${subtotal:.2f}")
sales_tax = float(subtotal) * sales_tax_rate / 100
print(f"Sales Tax: ${sales_tax:.2f}")
tip = float(input(f""" 
15% = {.15 * subtotal:.2f} 
20% = {.20 * subtotal:.2f}
25% = {.25 * subtotal:.2f}
\nHow much would you like to tip?"""))
total = subtotal + sales_tax + tip
print(f"Total: ${total:.2f}")

payment_amount = float(input(f"What is the payment amount? "))
print(f"Change: ${payment_amount - total}")


