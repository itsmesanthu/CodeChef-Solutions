# PYTH100

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Table of any number

Listen

Write a program which does the following

- Create a variable n and store the user defined input from console in n
- Output to the console the multiplication table for n up to 10 In the previous module we manually entered each row of the table In this problem - use for loops to generate the table
### Sample 1:
Input
Output

```
5
```

```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T15:58:32.337Z  

```py
# Update the code below

n = int(input())
for i in range(1,11,1):
    print(n,"x",i,"=",n*i)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH100)