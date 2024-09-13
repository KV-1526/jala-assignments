def check_even_odd(num):
  """Checks whether a number is even or odd using a switch statement.

  Args:
    num: The number to check.
  """

  match num % 2:
    case 0:
      print(f"{num} is even.")
    case 1:
      print(f"{num} is odd.")
    case _:
      print("Invalid input.")

# Example usage:
num = 15
check_even_odd(num)