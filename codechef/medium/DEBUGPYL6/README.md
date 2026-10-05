# DEBUGPYL6

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Runtime error

Listen

We saw two different syntax errors in the last lesson.
There are many different types of syntax errors, but they are generally easiest to debug as the error description clearly explains what needs to be fixed.

Let us now learn about  **`Runtime errors`** 

### Runtime error

Runtime error occurs when your syntax is correct but the compiler (or interpreter in case of Python), is still not able to run the code due to an error.

Example :-

```
a = 5
b = 0
c = a / b

```

If you run the above code, you will get this error.

```
Traceback (most recent call last):
  File "/mnt/sol.py", line 3, in <module>
    c = a / b
        ~~^~~
ZeroDivisionError: division by zero

```

There is an error in line 3 because we are trying to divide 5 by 0 which is not possible.

### Task
- There is a sample code present in IDE, which inputs two number and prints their division.
- If you run the code for a test case like 3 0 you will get the runtime error.
- To fix it, add an if condition which checks if the value of b is 0 and output infinity directly. Otherwise output the result of integer division using //.
### Sample 1:
Input
Output

```
3 0
```

```
infinity
```

### Sample 2:
Input
Output

```
5 2
```

```
2
```

### Explanation:

5 // 2 = Rounded down value of 5 / 2 - hence output is 2.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T14:47:59.932Z  

```py
# Add an if /else condition to the code below

a, b = map(int, input().split())
if b == 0:
    print("infinity")
else:
    print(a // b)
```

---

[View on CodeChef](https://www.codechef.com/problems/DEBUGPYL6)