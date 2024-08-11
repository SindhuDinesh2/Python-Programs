# Define the grade conversion function
def get_grade(marks):
    if 90 <= marks <= 100:
        return 'A+'
    elif 80 <= marks < 90:
        return 'A'
    elif 70 <= marks < 80:
        return 'B+'
    elif 60 <= marks < 70:
        return 'B'
    elif 50 <= marks < 60:
        return 'C+'
    elif 40 <= marks < 50:
        return 'C'
    else:
        return 'F'

# Define a dictionary with student names as keys and subject marks as values
students = {
    'Alice': {'Math': 92, 'Science': 85, 'English': 88, 'History': 91, 'Art': 79},
    'Bob': {'Math': 67, 'Science': 74, 'English': 59, 'History': 82, 'Art': 88},
    'Charlie': {'Math': 45, 'Science': 55, 'English': 62, 'History': 48, 'Art': 50}
}

# Create a dictionary to store student grades
student_grades = {}

# Compute grades for each student
for student, subjects in students.items():
    grades = {subject: get_grade(marks) for subject, marks in subjects.items()}
    student_grades[student] = grades

# Output the student grades
for student, grades in student_grades.items():
    print(f"{student}: {grades}")
