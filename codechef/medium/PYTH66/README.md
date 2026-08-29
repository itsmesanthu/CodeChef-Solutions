# PYTH66

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Elif Statement

Listen

In the previous problems, you saw how your code can have two different flows using one if and one else condition.
Now what if you want to evaluate more than two conditions? In such case, one if and one else condition is not sufficient. That is where  **elif statements**  come in handy. Let's understand them in detail.

In short, in cases where you have to check for multiple conditions and run some code based on each, you have to use  **elif**.

The  **elif**  keyword means "if the previous conditions were not true, then try this condition".

The following example illustrates usage of  **elif**.

```
grade = 85

if grade >= 90:
    print("You got an A")
elif grade >= 80:
    print("You got a B")

# Output:
# You got a B

```

The code above works as follows

- If grade >= 90, then it will output: You got an A
- If grade is between 80 and 90 - it will output: You got a B
- If grade is less than 80 - there will be no output
### Task

Write a program which does the following

- Take two integers b and r as input
- Print "Rob scored higher marks than Bob", if r is greater than b
- Print "Bob & Rob both scored the same", if both b and r are equal
### Sample 1:
Input
Output

```
20
25
```

```
Rob scored higher marks than Bob
```

### Sample 2:
Input
Output

```
15
15
```

```
Bob & Rob both scored the same
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T13:13:59.199Z  

```py
b = int(input())
r = int(input())
if r>b:
    print("Rob scored higher marks than Bob")
elif r==b:
    print("Bob & Rob both scored the same")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH66)