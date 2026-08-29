# PYTHCL66

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Else Statement

Listen

The else keyword handles the case that don't meet the conditions specified in the if and elif statements. It's like a "none of the above" option in programming.

### Task

Some code is written in the editor.

- Create integer variables r and k - the weight of friends Ram and Karan
- Take user input for r and then k
- Output based on these conditions: If r is greater than k, output "Ram is heavier than Karan" If r is less than k, output "Karan is heavier than Ram" Otherwise, output "Ram & Karan have the same weight"

Your task is to complete the blanks in the code.

<img src=https://cdn.codechef.com/Learning/learn-python-new/ram-karan.png width=500px height=600px>

### Sample 1:
Input
Output

```
24 32
```

```
Karan is heavier than Ram
```

### Sample 2:
Input
Output

```
78 78
```

```
Ram & Karan have the same weight!
```

### Sample 3:
Input
Output

```
32 24
```

```
Ram is heavier than Karan.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T13:15:25.539Z  

```py
# Update the blanks in the code below to solve the problem

r, k = map(int, input().split())

if r>k:
    print("Ram is heavier than Karan")
elif r<k:
    print("Karan is heavier than Ram")
else:
    print("Ram & Karan have the same weight")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL66)