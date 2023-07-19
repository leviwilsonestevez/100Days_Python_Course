print("Welcome to the rollercoaster")
height = int(input("Whar is your height in cm?\n"))

if height >= 120:  # height = 20 Systax Error
    print("You can ride the rollercoaster")
    age = int(input("What is your name"))
    if age < 12:
        print("You have to pay $5")
    elif age <= 18:
        print("You have to pay $7")
    else:
        print("You have to pay $12")
# print("identation error is going to appear here")
else:
    print("Sorry, you have to grow in order to ride the rollercoaster")
