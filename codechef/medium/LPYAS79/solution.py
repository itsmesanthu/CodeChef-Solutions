# Given dictionary
student_grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 88, "John": 45}
n=input()
if n in student_grades:
    print(student_grades[n])
else:
    print("Not Found")