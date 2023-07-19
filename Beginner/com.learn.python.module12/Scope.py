# ##################Scope########################

# ########## LOCAL SCOPE #################
def drink_potion():
    potion_strength = 2
    print(f"potion strength : {potion_strength}")


drink_potion()
# print(potion_strength) potion_strength is a local scope variable

# ########## GLOBAL SCOPE #################
potion_strength = 0
runner_health = 1


def something() -> None:
    print(f"Something")


# There is not a block scope

enemies = ["Skeleton", "Zombie", "Alien"]
if len(enemies) > 2:
    new_enemy = enemies[0]
print(new_enemy)  # We can print new_enemy variable


# Modifying Global Scope into a function

def increase_enemies() -> None:
    global enemies
    print(f"You can modify enemies here {enemies}. With global word we are indicating the scope of the variable")


# Global Constants
PI = 3.1415926


