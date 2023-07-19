import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_number > 2 or user_number < 0:
    print("User lose")
game = [rock, paper, scissors]
user_choice = game[user_number]
pc_number = random.randint(0, 2)
pc_choice = game[pc_number]
print("User choice  : \n")
print(user_choice)
print("PC choice  : \n")
print(pc_choice)

if user_number == 0 and pc_number == 2:
    print("You win!")
elif pc_number == 0 and user_number == 2:
    print("You lose")
elif pc_number > user_number:
    print("You lose")
elif user_number > pc_number:
    print("You win!")
elif pc_number == user_number:
    print("It's a draw")
