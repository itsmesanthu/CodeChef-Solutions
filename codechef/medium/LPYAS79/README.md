# LPYAS79

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a dictionary  **student_grades**  where the keys are the names of students and the values are their corresponding grades.

Take a string input - the name of a student and print the grade of the student if his/her name is present in given dictionary else print  **Not Found**.

### Sample 1:
Input
Output

```
Bob
```

```
72
```

### Sample 2:
Input
Output

```
Elena
```

```
Not Found
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-30T12:51:07.910Z  

```py
# Given dictionary
student_grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 88, "John": 45}
n=input()
if n in student_grades:
    print(student_grades[n])
else:
    print("Not Found")
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS79)