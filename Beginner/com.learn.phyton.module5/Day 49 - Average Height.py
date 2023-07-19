# Example : 180 124 165 173 189 169 146
# Test : 156 178 165 171 187
total = 0
count = 0
student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total += student_heights[n]
    count += 1

average = round((total / count))
print(f"The average is {average}")
