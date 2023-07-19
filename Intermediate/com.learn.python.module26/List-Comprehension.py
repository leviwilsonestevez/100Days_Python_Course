numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [number ** 2 for number in numbers]

# Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]

# Write your code 👆 above:

print(result)

with open("file1.txt", mode="r") as file1:
    numbers_file1 = file1.read().splitlines()

with open("file2.txt", mode="r") as file2:
    numbers_file2 = file2.read().splitlines()

result = [int(number) for number in numbers_file1 if number in numbers_file2]
# Write your code above 👆

print(result)
