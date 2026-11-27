# LCPPCL115C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Odd numbers

Listen

### Task

Write a program to print odd numbers between $10$ to $20$ on separate lines:

- Think of where the loop should start from, declare a variable a and initialise it to that value.
- Use the while syntax to create a loop, Think of what condition would stop the loop when the iterator reaches its end. Think of how to adjust the value of the iterator within each iteration. Would it be incremented or decremented? By what value should it be incremented or decremented?
#### Expected output:

```
11
13
15
17
19

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T15:13:33.275Z  

```py
# cook your dish here
a=10
while a<20:
    if a%2!=0:
        print(a)
    a+=1
    
```

---

[View on CodeChef](https://www.codechef.com/problems/LCPPCL115C)