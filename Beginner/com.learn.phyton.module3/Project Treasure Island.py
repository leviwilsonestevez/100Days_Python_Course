print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input(f"You are at a crossroad, where do you want to go ? Type left or right").lower()

if (choice1 == "right" or choice1 == "r"):
    print("You have fell into a hole. Game over")
else:
    choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake. " +
        "Type 'wait' to wait for a boat. Type 'swin' to swin across ")
    if (choice2 == "wait" or choice2 == "w"):
        choice3 = input("You arrive at the island unharmed. There is a house " +
                        "with 3 doors. One red,one yellow and one blue ")
        if choice3=="red" or choice3=="r":
            print("Game Over. You chose red.")
        elif choice3=="yellow" or choice3=="y" :
            print("Game win!!!")
        elif choice3=="blue" or choice3=="b":
            print("Game over. You have chose blue.")
        else:
            print("You chose wrong. Game over")
    else:
        print("Game Over. You enter a room of beats.")