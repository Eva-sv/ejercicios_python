# Define the prices

tshirt_price = 10
sweatshirt_price = 20.5
cap_price = 5.5

# Ask the user for the quantity of each item

tshirt_quantity = int(input("How many T-shirts would you like?"))
sweatshirt_quantity = int(input("How many sweatshirts would you like?"))
cap_quantity = int(input("How many caps would you like?"))

# Calculate the total purchase

total_purchase = tshirt_price * tshirt_quantity + sweatshirt_price * sweatshirt_quantity + cap_price * cap_quantity

# Add 21% VAT

total_purchase_vat = total_purchase * 0.21 

# Show final price

final_price = total_purchase + total_purchase_vat

print("Total purchase", total_purchase)
print("VAT",total_purchase_vat)
print("Final price", final_price)





