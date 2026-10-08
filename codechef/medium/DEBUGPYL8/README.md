# DEBUGPYL8

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Incorrect Conditionals

Listen

`Incorrect conditionals` are one of the most common types of logical errors.
They occur when you put an incorrect condition in if-else.

### Example

The code below is supposed to do the following

- If an integer is even, then output even
- If an integer is odd, then output odd

```
n = 10

if n % 2 == 0:
    print("odd")
else:
    print("even")

```

The above code is incorrect because it outputs `odd` when the number is even.
Changing the IF condition will fix the error.

```
n = 10

if n % 2 != 0:
    print("odd")
else:
    print("even")

```

### Task

Given a program to check whether a number is greater than 5 or not.

- Run the code without changing anything, it will give wrong answer.
- Find the wrong condition and correct it.
### Sample 1:
Input
Output

```
5
```

```
the number is smaller than or equal to 5
```

### Sample 2:
Input
Output

```
6
```

```
the number is greater than 5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T09:27:59.202Z  

```py
#if condition is wrong it should be changed to n>5
n = int(input())

if n >5:
    print("the number is greater than 5")
else:
    print("the number is smaller than or equal to 5")

```

---

[View on CodeChef](https://www.codechef.com/problems/DEBUGPYL8)