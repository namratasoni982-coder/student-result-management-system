class Student:

    all_students = []

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    @classmethod
    def add_student(cls):
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = int(input("Enter marks: "))

        student = cls(name, roll, marks)
        cls.all_students.append(student)

        print("Student added successfully.")

    @classmethod
    def find_student_by_roll(cls, roll):
        for student in cls.all_students:
            if student.roll_number == roll:
                return student
        return None

    @classmethod
    def update_student_marks(cls):
        roll = input("Enter roll number: ")

        student = cls.find_student_by_roll(roll)

        if student:
            new_marks = int(input("Enter new marks: "))
            student.marks = new_marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No students found.")
            return

        for student in cls.all_students:
            print(
                "Name:", student.name,
                "Roll:", student.roll_number,
                "Marks:", student.marks
            )


while True:

    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Show All")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        Student.add_student()

    elif choice == "2":
        Student.update_student_marks()

    elif choice == "3":
        Student.show_all_students()

    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")