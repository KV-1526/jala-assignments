def print_gender(gender):
  """Prints the gender based on the given code.

  Args:
    gender: The gender code (M or F).
  """

  match gender.upper():
    case "M":
      print("Male")
    case "F":
      print("Female")
    case _:
      print("Invalid gender code.")

# Example usage:
gender_code = "F"
print_gender(gender_code)