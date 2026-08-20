name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input("Enter subject " + str(i + 1) + " marks: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Result ---")
print("Student:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
