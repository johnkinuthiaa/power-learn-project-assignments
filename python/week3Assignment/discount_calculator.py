def  calculate_discount(price, discount_percent) :
    if discount_percent>=20:
        return price -price*(discount_percent/100)
    else:
        return price

original_price =float(input("Enter the original price of the item: "))
discount =float(input("Enter the discount value: "))
print(f"The final price is {calculate_discount(original_price,discount)}")