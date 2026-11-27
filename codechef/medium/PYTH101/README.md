# PYTH101

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Factorial of any number

Listen

Write a program that does the following

- Declare an integer variable num and initialize it to a user defined input
- Output to the console the factorial of num Remember to use loops for this problem Factorial of a number n is the product of all the numbers from 1 to n Factorial of a number(n) = n × (n-1) ×... 2 × 1
### Sample 1:
Input
Output

```
6
```

```
The factorial of the given number is: 720

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T15:59:47.027Z  

```py
# Debug the code below to output the factiorial of a user defined input n

n = int(input())

i = 1
factorial = 1

while i <= n:
    factorial = i* factorial
    i = i + 1
    
print("The factorial of the given number is:", factorial)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH101)