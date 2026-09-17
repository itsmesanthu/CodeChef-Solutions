# PYTHCL63

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Indentation

Listen

Let us take a look at the code from last problem.

```
age = int(input())

if age >= 18:
    print("Old enough to vote")
else:
    print("Not old enough to vote")

```

Two things to note here:

- There is some space before the print statements.
- There is a colon (:) after if and else statements.

The space before print is called  **indentation**. Indentation is used to define scope in Python. Because of the space before `print`, Python knows that it has to execute the print statement if the condition becomes True.

The colon after IF and ELSE is also part of the syntax, you will get an error if you forget it.

### Task

You need to do the following

- Run the code as is and read the error that you get
- Add space before the print syntax and then re-run the code

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-17T17:17:31.317Z  

```py
r = 1000
w = 3222
if r > w:
#This code will not run due to improper indentation
    print("White balls are out of stock")  
else:
#Fix the error by putting a space before both print
    print("Your order is Confirmed")


```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL63)