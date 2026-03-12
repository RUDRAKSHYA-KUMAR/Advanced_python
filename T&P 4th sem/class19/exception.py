class StudentGradeSystem:

    def __init__(self):
        self.students = {}  

    
    def add_student(self):
        try:
            sid = int(input("Enter Student ID: "))

            if sid in self.students:
                raise Exception("Student ID already exists!")

            grade = input("Enter Grade: ")

            if grade.strip() == "":
                raise ValueError("Grade cannot be empty!")

            self.students[sid] = grade
            print("Student added successfully.\n")

        except ValueError:
            print("Invalid input! Student ID must be a number and grade cannot be empty.\n")

        except Exception as e:
            print(e, "\n")

    
    def update_student(self):
        try:
            sid = int(input("Enter Student ID to update: "))

            if sid not in self.students:
                raise KeyError("Student ID not found!")

            grade = input("Enter new grade: ")

            if grade.strip() == "":
                raise ValueError("Grade cannot be empty!")

            self.students[sid] = grade
            print("Grade updated successfully.\n")

        except ValueError:
            print("Invalid grade input!\n")

        except KeyError as e:
            print(e, "\n")

    
    def delete_student(self):
        try:
            sid = int(input("Enter Student ID to delete: "))

            if sid not in self.students:
                raise KeyError("Student ID not found!")

            del self.students[sid]
            print("Student deleted successfully.\n")

        except ValueError:
            print("Student ID must be numeric.\n")

        except KeyError as e:
            print(e, "\n")

    
    def display_students(self):
        if not self.students:
            print("No records found.\n")
        else:
            print("\nStudent Records:")
            for sid, grade in self.students.items():
                print("ID:", sid, " Grade:", grade)
            print()



system = StudentGradeSystem()

while True:
    print("------ Student Grade Management ------")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.update_student()

    elif choice == "3":
        system.delete_student()

    elif choice == "4":
        system.display_students()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Try again.\n")