def perform_operation(num1, num2, operator):
  """Performs the specified operation on two numbers.

  Args:
    num1: The first number.
    num2: The second number.
    operator: The operator to perform (+, -, *, x, /).

  Returns:
    The result of the operation.
  """

  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == 'x':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  else:
    raise ValueError("Invalid operator: {}".format(operator))

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, x, /): ")

# Perform the operation and display the result
result = perform_operation(num1, num2, operator)
print("{} {} {} = {}".format(num1, operator, num2, result))