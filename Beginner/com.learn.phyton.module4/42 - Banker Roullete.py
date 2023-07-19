import random

names_string = input("Put all names of the table separates with comma \n")
names = names_string.split(",")
chose_name = random.randint(0, names.__len__() - 1)
# Alternative Solution
# chose_name = random.randint(o,len(names)-1)
# chose_name = random.choice(names)
person_who_will_pay = names[chose_name]
print(f"{person_who_will_pay} is going to buy the meal today!")

