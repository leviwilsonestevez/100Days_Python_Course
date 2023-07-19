actual_age=input("What is your current age (Expected age in Mexico is 85): \n")
actual_age=int(85)-int(actual_age)
x=int(actual_age)*365
y=int(actual_age)*52
z=int(actual_age)*12
print(f"You have {x} days {y} weeks and {z} months to left")