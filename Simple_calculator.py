def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

print("Welcome to Simple Calculator!")
print("Operations available:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter operation number (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '1':
    print("Result:", add(num1, num2))
elif operation == '2':
    print("Result:", subtract(num1, num2))
elif operation == '3':
    print("Result:", multiply(num1, num2))
elif operation == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")