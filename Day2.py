class students:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}

    def add_grades(self, subject, marks):
        self.grades[subject] = marks
    
    def cal_avg(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values())/len(self.grades)
    # Minor edit to trigger new git commit

    
    def assign_grades(self):
        avg = self.cal_avg()
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "F"

    def apply_bonus(self, lambda_func):
        for subject in self.grades:
            self.grades[subject] = min(100, lambda_func(self.grades[subject]))
    
    def generate_report(self):
        report_lines = [
           f"Report Card:",
           f"Name: {self.name}",
           f"Age: {self.age}"
        ]

        for subject, marks in self.grades.items():
            report_lines.append(f"subject: {marks}")
        
        avg = self.cal_avg()
        letter_grade = self.assign_grades()


        report_lines.append(f"Average: {avg:.2f}")
        report_lines.append(f"Grade: {letter_grade}")

        return "\n".join(report_lines)
    
    def save_to_file(self, filename):
        report = self.generate_report()
        with open (filename, "w") as file:
            file.write(report)
        print("Report saved successfully")
    
    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
            print("\n--- Report Loaded ---")
            print(content)
        except FileNotFoundError:
            print("File not found!")


name = input("Enter student's name: ")
age = int(input("Enter age: "))

student = students(name, age)

for subject in ["Math", "English", "Urdu"]:
    marks = int(input(f"Enter marks for {subject}: "))
    student.add_grades(subject, marks)

apply_bonus = input("Add 5 bonus marks to all subjects? (yes/no): ").strip().lower()

if apply_bonus == "yes":
    bonus_lambda = lambda x: x + 5
    student.apply_bonus(bonus_lambda)

filename = f"{student.name}_report.txt"
student.save_to_file(filename)
students.load_from_file(filename)