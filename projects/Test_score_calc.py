print("Test Score Calculator")

student_name = input("Enter the student's name: ")

score_1 = float(input("Enter the first score: "))
score_2 = float(input("Enter the second score: "))
score_3 = float(input("Enter the third score: "))

total_score = score_1 + score_2 + score_3
average_score = total_score / 3

if average_score >= 70:
    result = "Passed"
else:
    result = "Failed"

print(f"Student: {student_name}")
print(f"Average score: {average_score: .2f}")
print(f"Result: {result}")