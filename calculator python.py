import math
def calculate():
  operation = input("What operation would you like to perform (+, -, *, /, sqrt, **)? ")
  if operation == 'sqrt':
    num = float(input("Enter a number: "))
    result = math.sqrt(num)
  elif operation == '**':
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    result = base ** exponent
  else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if operation == '+':
      result = num1 + num2
    elif operation == '-':
      result = num1 - num2
    elif operation == '*':
      result = num1 * num2
    elif operation == '/':
      result = num1 / num2
  print("The result is", result)

calculate()
