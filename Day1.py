name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

subjects = {}

for i in range(3):
    sub = input("Enter The Name of Subject: ")
    marks = int(input("Enter The The Marks of the Subject: "))
    subjects[sub] = marks

# def cal_Avg(subjects):
#     return sum(marks)/3

avg = lambda subjects: sum(subjects.values())/3
average = avg(subjects)

# Minor edit to trigger new git commit

print(f"\nName: {name}")
print(f"Age: {age}")
print("Subjects and Marks:", subjects)
print("Average Marks:", avg(subjects))

def get_grade(average):
    if average >= 80 :
        return "A"
    elif 60 <= average < 79 :
        return "B"
    elif 40 <= average < 59 :
        return "C"
    elif average < 40 :
        return "F"
    else :
        return "Error in Avg!"

print("Grade:", get_grade(average))

yes_NO = input("\nDo you want a bonus? (yes/no): ")

bonus = lambda answer, average : ((average + 5), "Bonus Applied") if answer.lower() == "yes" else "No Bonus"


new_avg, message = bonus(yes_NO, average)

print(message)
print("New Average Marks:", new_avg)
print("New Grade:", get_grade(new_avg))