# Discount calculation

def calculate_discount(price, discount_percent):

    if discount_percent > 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price

p = float(input("Enter the price: "))
discount = float(input("Enter the discount percentage: "))

result = calculate_discount(p, discount)
print(f"The final price after discount is: {result}")