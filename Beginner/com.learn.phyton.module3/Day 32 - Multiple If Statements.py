print("Welcome to the rollercoaster")
height = int(input("Whar is your height in cm?\n"))

if height >= 120:  # height = 20 Systax Error
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill=5
        print("Child ticket are $5")
    elif age <= 18:
        bill=7
        print("Youth ticket are $7")
    else:
        bill=12
        print("Adults tickets are $12")
    wants_photo=input("What photo Yes (Y) or No(N)? \n")
    if wants_photo == "Y" or wants_photo == "y":
        bill +=3
        print(f"the total bill is {bill}")
    else:
        print(f"the total bill is {bill}")
# print("identation error is going to appear here")
else:
    print("Sorry, you have to grow in order to ride the rollercoaster")
