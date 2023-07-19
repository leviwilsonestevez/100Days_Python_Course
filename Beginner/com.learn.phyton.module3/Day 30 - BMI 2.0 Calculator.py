height = input("Enter your height in m :")
weight = input("Enter your mass in kg :")
bmi = round((float(weight) / (float(height) ** 2)), 1)

if bmi < 18.5:
    print(f"You bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight ")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese ")
else:
    print(f"Ypur bmi is {bmi}, you are clinically obese")
