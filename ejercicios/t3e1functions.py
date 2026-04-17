
# We define functions that take and return parameters

def Calculate_VAT(total_price, vat_percentage):
    result = total_price * vat_percentage
    return result 

def Calculate_Total_Price (unit_price, produt_quantity):
    result = unit_price * produt_quantity
    return result

def Calculate_discount (total_price, discount_percentage):
    result = total_price * discount_percentage
    return result

def Calculate_final_price (total_price, discount,vat):
    result = (total_price - discount) + vat
    return result



# We store the name of each function

unit_price = int (input("Put the unit price: "))
produt_quantity = int (input("Put the product quantity: "))
vat_percentage = float (input("Put the vat on percentage: "))
product_name = input(" Put the product name: ")
discount_percentage = float (input("Put the discount on percentage: "))

# We call the functions

total_price = Calculate_Total_Price(unit_price, produt_quantity)
discount = Calculate_discount(total_price, discount_percentage)
vat = Calculate_VAT(total_price, vat_percentage)
final_price = Calculate_final_price (total_price, discount,vat)

print(final_price)








