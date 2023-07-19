student_scores = [78, 65, 120, 89, 86, 55, 91, 64, 89]
high_score = max(student_scores)
print(f"The highest score in the class is: {high_score}")

# Real Challenge
high_score = 0
for student_score in student_scores:
    if student_score > high_score:
        high_score = student_score
print(f"The highest score in the class is: {high_score}")
