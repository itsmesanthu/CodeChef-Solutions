# PYTHCL64

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### If Statement

Listen

The  **`else`**  statement is optional.

Here is an example

```
grade = 95
if grade >= 90:
    print("You got an A")

# Output:
# You got an A

```

In this example, the if condition checks whether the grade is greater than or equal to 90. If the condition is True, the print statement inside the if block is executed, and it prints "`You got an A`".

If the condition is False, the program skips the if block and moves on to the next part of the code (if any). Since there is no else block in this example, nothing happens if the condition is False.

The else block is useful when you want to specify an action if the if condition is not met, but it's not necessary if you only need to perform an action when the condition is True.

### Task

Write a program which does the following

- Take input for two integer variables a & b
- Output "Coding is Fun" to the console if a is greater than b
### Sample 1:
Input
Output

```
25
20
```

```
Coding is Fun
```

### Explanation:

25 is greater than 20, so we print 'Coding is Fun'

### Sample 2:
Input
Output

```
20
20
```

```
 
```

### Explanation:

Since there is no else statement nothing happens if the condition is False. Hence the output is empty

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T13:11:09.861Z  

```py
a=int(input())
b=int(input())
if a>b:
    print("Coding is Fun")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL64)