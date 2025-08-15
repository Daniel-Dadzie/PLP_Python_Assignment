🏷️ Discount Calculation Program
📌 Overview

This Python program calculates the final price of an item after applying a discount — but only if the discount percentage is greater than 20%.
If the discount is 20% or less, the original price remains unchanged.

✨ Features

✅ Accepts user input for price and discount percentage
✅ Applies discount only if it’s more than 20%
✅ Displays the final price clearly
✅ Works with decimal values

🛠 How It Works

1️⃣ User enters:

The price of the item

The discount percentage
2️⃣ Program checks:

If discount > 20% → applies the discount

Else → keeps original price
3️⃣ Final price is printed to the console

🧩 Code Explanation
def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price


Function: calculate_discount(price, discount_percent)

Logic:

If discount_percent is greater than 20, calculate discount and subtract from price.

Else, return the original price.

▶️ Example Run
Enter the price: 1000  
Enter the discount percentage: 25  
The final price after discount is: 750.0

📌 Notes

📉 Discounts must be more than 20% to take effect.

💡 Works with both whole numbers and decimal values for price & discount.

📂 How to Run

Make sure you have Python 3 installed.

Save the code in a file called discount_calculator.py.

Open a terminal and run:

python discount_calculator.py