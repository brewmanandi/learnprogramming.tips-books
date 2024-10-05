# Simple command-line calculator

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for the operation
operation = input("Enter operation (+, -, *, /): ")

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed"
else:
    result = "Invalid operation"

# Display the result
print("The result is:", result)
