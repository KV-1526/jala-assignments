def increment(num):
  """Increments a number by 1.

  Args:
    num: The number to increment.

  Returns:
    The incremented number.
  """

  return num + 1

def decrement(num):
  """Decrements a number by 1.

  Args:
    num: The number to decrement.

  Returns:
    The decremented number.
  """

  return num - 1

# Example usage:
num = 5
incremented_num = increment(num)
decremented_num = decrement(num)

print("Incremented number:", incremented_num)
print("Decremented number:", decremented_num)