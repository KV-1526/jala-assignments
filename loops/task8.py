def is_armstrong_number(num):
  """Checks if a number is an Armstrong number.

  Args:
    num: The number to check.

  Returns:
    True if the number is an Armstrong number, False otherwise.
  """

  temp = num
  result = 0
  while temp > 0:
    digit = temp % 10
    result += digit ** len(str(num))
    temp //= 10

  return num == result

# Example usage:
num = 153
if is_armstrong_number(num):
  print(f"{num} is an Armstrong number.")
else:
  print(f"{num} is not an Armstrong number.")