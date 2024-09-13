def is_prime(num):
  """Checks if a number is prime.

  Args:
    num: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """

  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False

  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6

  return True

# Example usage:
num = 17
if is_prime(num):
  print(f"{num} is a prime number.")
else:
  print(f"{num} is not a prime number.")