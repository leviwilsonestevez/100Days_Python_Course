# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
check_word = "truelove"
list = {}
for element in check_word:
    total = name1.count(element) + name2.count(element)
    list[element] = total
one = list["t"] + list["r"] + list["u"] + list["e"]
two = list["l"] + list["o"] + list["v"] + list["e"]
love_calculation = int(str(one) + str(two))
if love_calculation > 90 or love_calculation < 10:
    print(f"Your score is {love_calculation}, you go together like coke and mentos.")
elif love_calculation >= 40 and love_calculation <= 50:
    print(f"Your score is {love_calculation}, you are alright together.")
else:
    print(f"Your score is {love_calculation}.")
