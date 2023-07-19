import random

names = ["Alex ", "Beth", "Dave", "Caroline", "Eleanor", "Freddy"]
students_score = {name: random.randint(1, 10) for name in names}
passed_students = {student: score for (student, score) in students_score.items() if score > 5}
print("Passed Students = ", passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Write your code below:
result = {word: len(word) for word in sentence.split()}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# Write your code 👇 below:
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
