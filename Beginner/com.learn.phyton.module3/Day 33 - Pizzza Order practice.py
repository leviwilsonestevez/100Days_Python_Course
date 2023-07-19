# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?\n")
add_pepperoni = input("Do you want pepperoni? Y or N ?\n")
extra_cheese = input("Do you want extra cheese? Y or N ? \n")
# 🚨 Don't change the code above 👆
bill=0
if size == "S" or size == "s":
    bill = 15
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 2
        if extra_cheese == "Y" or extra_cheese == "y":
            bill += 1
if size == "M" or size == "m":
    bill = 20
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 3
        if extra_cheese == "Y" or extra_cheese == "y":
            bill += 1
if size == "L" or size == "l":
    bill = 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 3
        if extra_cheese == "Y" or extra_cheese == "y":
            bill += 1
print(f"Your final bill is: ${bill}.")
#Write your code below this line 👇