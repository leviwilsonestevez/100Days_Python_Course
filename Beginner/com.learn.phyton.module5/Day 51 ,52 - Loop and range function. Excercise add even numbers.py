for i in range(1, 21):
    print(i)
for number in range(1, 20, 3):
    print(number)

# Gauss'sProblem
total = 0
for d in range(1, 101):
    total += d
print(f"Adding first 100 numbers the result is {total}")

# Adding even numbers
total = 0
for even_sum in range(2, 101, 2):
    total += even_sum
print(f"Adding first even numbers the result is {total}")
