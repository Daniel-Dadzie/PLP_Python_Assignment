🧮 Basic Calculator Program
📌 Overview

This Python program is a simple calculator that performs addition, subtraction, multiplication, and division based on user input.
It takes two numbers and an operator from the user, processes the calculation, and displays the result.

✨ Features

✅ Accepts user input for two numbers and an operator
✅ Supports the four basic arithmetic operations: +, -, *, /
✅ Handles division by zero with an error message
✅ Displays the result in a clear format

🛠 How It Works

1️⃣ The program prompts the user to enter:

First number

Second number

Operator (+, -, *, /)
2️⃣ It checks which operation to perform based on the operator input.
3️⃣ If division is selected and the second number is 0, it shows an error message.
4️⃣ The result is printed in the format:

<first number> <operator> <second number> = <result>

🧩 Code Explanation
if operator == "+":
    result = numb1 + numb2
elif operator == "-":
    result = numb1 - numb2
elif operator == "*":
    result = numb1 * numb2
elif operator == "/":
    if numb2 == 0:
        print("Division by zero is invalid!")
        result = None
    else:
        result = numb1 / numb2
else:
    print("Invalid operator selection!")
    result = None


Checks the entered operator.

Performs the corresponding calculation.

Prevents division when the second number is zero.

▶️ Example Run
Enter first number: 10  
Enter second number: 5  
Enter the operator (+, -, *, /): *  
10 * 5 = 50

📂 How to Run

Make sure you have Python 3 installed.

Save the program as calculator.py.

Open a terminal or command prompt in the file's location.

Run the program:

python calculator.py
