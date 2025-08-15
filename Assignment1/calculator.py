# Basic Calculator Program

numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))

operator = input("Enter the operator (+, -, *, /): ")

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

if result is not None:
    print(f"{numb1} {operator} {numb2} = {result}")
