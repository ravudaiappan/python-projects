#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_password = []
letters_length = len(letters)

for ltr in range(0, nr_letters):
  letter_index = random.randint(1, letters_length)
  letter_password.append(letters[letter_index -1])
print(letter_password)

symbol_password = []
symbol_length = len(symbols)

for ltr in range(0, nr_symbols):
  symbol_index = random.randint(1, symbol_length)
  symbol_password.append(symbols[symbol_index -1])
print(symbol_password)

number_password = []
number_length = len(numbers)

for ltr in range(0, nr_numbers):
  number_index = random.randint(1, number_length)
  number_password.append(numbers[number_index -1])
print(number_password)

mystring = ''
mystring= ''.join(symbol_password)
mystring += ''.join(letter_password)
mystring += ''.join(number_password)
print(mystring)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

rand_mystring = list(mystring)
random.shuffle(rand_mystring)
final_pass = ''.join(rand_mystring)
print(final_pass)
