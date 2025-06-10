# -----------------------------------------------
# 🧑‍🎓 Student Grading System using OOP & File Handling
# -----------------------------------------------

import os  # For file operations
import json  # For saving/loading structured data


# -----------------------------------------------
# 📘 Student Class - Represents an individual student
# -----------------------------------------------

class Student:
    """Represents a student and their academic records."""

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # Dictionary: subject -> score
        self.total = sum(marks.values())
        self.percentage = self.total / len(marks)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        """Determine grade based on percentage."""
        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 80:
            return 'A'
        elif self.percentage >= 70:
            return 'B'
        elif self.percentage >= 60:
            return 'C'
        elif self.percentage >= 50:
            return 'D'
        else:
            return 'F'

    def to_dict(self):
        """Convert student data to dictionary format for saving."""
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'marks': self.marks,
            'total': self.total,
            'percentage': self.percentage,
            'grade': self.grade
        }

    def __str__(self):
        """Nicely formatted string representation of the student."""
        marks_str = "\n".join([f"{subject}: {score}" for subject, score in self.marks.items()])
        return (
            f"\nName: {self.name}\n"
            f"Roll No: {self.roll_no}\n"
            f"{marks_str}\n"
            f"Total: {self.total}\n"
            f"Percentage: {self.percentage:.2f}%\n"
            f"Grade: {self.grade}"
        )


# -----------------------------------------------
# 🗃️ GradingSystem Class - Manages all students
# -----------------------------------------------

class GradingSystem:
    """Handles student records and grading operations."""

    def __init__(self, filename="grades.txt"):
        self.filename = filename
        self.students = []  # List to store Student objects
        self.load_data()

    def load_data(self):
        """Load student records from file if available."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    self.students = [Student(d['name'], d['roll_no'], d['marks']) for d in data]
            except Exception as e:
                print(f"⚠️ Error loading data: {e}")

    def save_data(self):
        """Save student records to file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([s.to_dict() for s in self.students], file, indent=4)
        except Exception as e:
            print(f"⚠️ Error saving data: {e}")

    def add_student(self):
        """Input and add a new student record."""
        try:
            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")
            num_subjects = int(input("How many subjects? "))
            marks = {}
            for _ in range(num_subjects):
                subject = input("Subject name: ")
                score = float(input(f"Marks for {subject}: "))
                marks[subject] = score

            student = Student(name, roll_no, marks)
            self.students.append(student)
            print("✅ Student record added successfully.")
        except Exception as e:
            print(f"❌ Error adding student: {e}")

    def view_all_students(self):
        """Display all student records."""
        if not self.students:
            print("📭 No student records available.")
        else:
            print("\n📄 Student Records:")
            for idx, student in enumerate(self.students, 1):
                print(f"\n--- Student {idx} ---")
                print(student)

    def search_student(self, roll_no):
        """Search for a student by roll number."""
        found = [s for s in self.students if s.roll_no == roll_no]
        if found:
            print("\n🎯 Student Found:")
            print(found[0])
        else:
            print("❌ Student not found.")

    def menu(self):
        # -----------------------------------------------
        # 🧭 CLI Menu Loop for User Interaction
        # -----------------------------------------------
        while True:
            print("\n========= 📊 Student Grading Menu =========")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student by Roll No")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.add_student()

            elif choice == '2':
                self.view_all_students()

            elif choice == '3':
                roll_no = input("Enter Roll Number to search: ")
                self.search_student(roll_no)

            elif choice == '4':
                self.save_data()
                print("💾 Student records saved. Goodbye!")
                break

            else:
                print("⚠️ Invalid option. Please choose 1-4.")


# -----------------------------------------------
# 🚀 Program Entry Point
# -----------------------------------------------
if __name__ == "__main__":
    system = GradingSystem()
    system.menu()
# -----------------------------------------------
# 🧑‍🎓 Student Grading System using OOP & File Handling