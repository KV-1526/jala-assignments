alphabet = input("Enter any alphabet: ")

if alphabet.isalpha():
  if alphabet.lower() in "aeiou":
    print("The alphabet is a vowel")
  else:
    print("The alphabet is a consonant")
else:
  print("Please enter a valid alphabet")