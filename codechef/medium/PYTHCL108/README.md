# PYTHCL108

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### User input Loop

Listen

Given an integer `N` as input.
You need to output the numbers from 0 to (N-1) on separate lines.

### Task
- Declare a variable num and store a user defined input from the console in it
- Declare a variable a and initialize it to 0
- Use the while syntax to create a loop, output the following to the console Print a in separate lines as long as it is less than num. Increment a by 1 in each iteration.
### Sample 1:
Input
Output

```
10
```

```
0
1
2
3
4
5
6
7
8
9
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T15:17:54.897Z  

```py
# Update your code below this line

num = int(input())
i=0
while i<num:
    print(i)
    i+=1
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL108)