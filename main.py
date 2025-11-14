# Student class 
class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    # Add a grade
    def add_grade(self, grade):
        self.grades.append(grade)

    # Calculate average grade
    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    # Return grades as a tuple
    def grades_tuple(self):
        return tuple(self.grades)

    # Display student info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.average_grade():.2f}\n")


# Create 3 students (you can change names/emails)
student1 = Student("David", "david@example.com", [85, 90])
student2 = Student("Fabiola", "fabiola@example.com", [78, 92])
student3 = Student("Stephanie", "stephanie@example.com", [88, 76])

# Add 2 new grades for each student
student1.add_grade(95)
student1.add_grade(80)

student2.add_grade(84)
student2.add_grade(91)

student3.add_grade(89)
student3.add_grade(94)

# Display info for each student
student1.display_info()
student2.display_info()
student3.display_info()

# Dictionary mapping email -> student
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Function to get student by email
def get_student_by_email(email):
    return student_dict.get(email, "Student not found")

# Show unique grades across all students
all_grades = set(student1.grades + student2.grades + student3.grades)
print("Unique grades across all students:", all_grades)

# Demonstrate tuple 
try:
    t = student1.grades_tuple()
    t[0] = 100
except TypeError:
    print("Tuples are immutable. Cannot change a grade in the tuple.\n")

# Remove last grade from each student
student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

# Show first and last grade, and number of grades
for s in [student1, student2, student3]:
    if s.grades:
        print(f"{s.name}'s first grade: {s.grades[0]}")
        print(f"{s.name}'s last grade: {s.grades[-1]}")
        print(f"{s.name} has {len(s.grades)} grades\n")
