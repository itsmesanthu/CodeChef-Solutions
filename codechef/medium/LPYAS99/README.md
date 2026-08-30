# LPYAS99

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to declare and accept an list of $N$(**will always be greater than 3**) space separate integers.
Calculate the  **multiplication**  of the 1st and 3rd elements of the list and output the same to the console.

Check the sample input / output below for further clarity.

### Sample 1:
Input
Output

```
10 12 25 9 20
```

```
250
```

### Explanation:

Here first element is 10 and 3rd element is 25, Hence 10 x 25 = 250

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-30T12:57:44.322Z  

```py
n=list(map(int,input().split()))
res=n[0]*n[2]
print(res)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS99)