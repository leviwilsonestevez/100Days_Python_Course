# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

chosen_pass = []
for i in range(1, nr_letters + 1):
    # chosen_letter = letters[random.randint(0, len(letters) - 1)]
    chosen_letter = random.choice(letters)
    chosen_pass += chosen_letter

for i in range(1, nr_symbols + 1):
    # chosen_symbol = symbols[random.randint(0, len(symbols) - 1)]
    chosen_symbol = random.choice(symbols)
    chosen_pass += chosen_symbol

for i in range(1, nr_numbers + 1):
    # chosen_number = numbers[random.randint(0, len(numbers) - 1)]
    chosen_number = random.choice(numbers)
    chosen_pass += chosen_number
random.shuffle(chosen_pass)

password = ""
for char in chosen_pass:
    password += char

print(f"Here is your password : {password}")
