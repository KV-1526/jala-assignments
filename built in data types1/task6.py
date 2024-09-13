character = input("Enter a character: ")

if character.isalpha() and character.islower():
  if character in "aeiou":
    print("It is a lowercase vowel")
  else:
    print("It is a lowercase consonant")
elif character.isdigit():
  print("It is a digit")
else:
  print("It is a symbol")