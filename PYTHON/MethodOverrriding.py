class Student:
    def __init__(self, name, num_subjects):
        self.name = name
        self.num_subjects = num_subjects
        self.subjects = []
        self.marks = []

    def input_details(self):
        print(f"Enter details for {self.name}:")
        for i in range(self.num_subjects):
            subject_name = input(f"Enter name of subject {i+1}: ")
            marks = float(input(f"Enter marks for {subject_name}: "))
            self.subjects.append(subject_name)
            self.marks.append(marks)

    def total_marks(self):
        pass

    def grade(self):
        pass


class ReportCard(Student):
    def __init__(self, name, num_subjects):
        super().__init__(name, num_subjects)

    def total_marks(self):
        return sum(self.marks)

    def grade(self):
        total = self.total_marks()
        percentage = (total / (self.num_subjects * 100)) * 100

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 35:
            return "D"
        else:
            return "F"

    def show_rc(self):
        print(f"\nName: {self.name}")
        print("Subjects and Marks:")
        for i in range(self.num_subjects):
            print(f"{self.subjects[i]}: {self.marks[i]}")

        total = self.total_marks()
        print(f"\nTotal Marks: {total}/{self.num_subjects * 100}")
        print(f"Grade: {self.grade()}")



name = input("Enter student name: ")
num_subjects = int(input("Enter number of subjects: "))

student = ReportCard(name, num_subjects)
student.input_details()
student.show_rc()
