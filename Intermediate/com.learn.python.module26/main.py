import random
import string

numbers = [1, 2, 3]
# List Comprehension
new_list = [i + random.randint(0, 10) for i in numbers]
print("New list ", new_list)
name = "Levis"
name_list = [random.choice(string.ascii_lowercase) for letter in name]
print(name_list)
numbers_list = [n * 2 for n in range(1, 5)]
print(numbers_list)
students = ["Markwqer", "Ambersad", "Todderwt", "Anita", "Sandy", "Tedd"]
short_names = [name for name in students if len(name) < 5]
long_names = [name.upper() for name in students if len(name) > 5]
print(short_names)
print(long_names)
