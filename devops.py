class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_average(self):
        return self.marks  # Assuming marks is already average

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())
        print("------------------------")


def main():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details for Student {i + 1}")

        name = input("Name: ")
        roll = int(input("Roll Number: "))
        marks = float(input("Marks: "))

        students.append(Student(name, roll, marks))

    print("\n--- Student Details ---")
    for student in students:
        student.display_details()


if __name__ == "__main__":
    main()
