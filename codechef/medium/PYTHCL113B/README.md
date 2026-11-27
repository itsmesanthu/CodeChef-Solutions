# PYTHCL113B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Two range arguments

Listen

Another way to use the range function is by providing two arguments: `start and stop`.
When you use two arguments in the `range(start, stop)` function, it generates a sequence of numbers starting from the start value up to, but not including, the stop value.

```
for i in range(2, 6):
    print(i)

```

 **Output** :

```
2
3
4
5
# Start: The sequence starts at the start value (inclusive). In this example, it starts at 2.
# Stop: The sequence ends at the stop value (exclusive). In this example, it stops before 6.

```

So, the range(2, 6) function generates the numbers 2, 3, 4, and 5. The start value is included in the sequence, but the stop value is not.

### Task

Write a program which does the following

- Accepts a user-defined input as the variable num
- Output all positive integers from 1 till num - num inclusive - on a separate line
### Sample 1:
Input
Output

```
5
```

```
1
2
3
4
5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T15:54:08.542Z  

```py
# Update your code below this line
n=int(input())
for i in range(1,n+1):
    print(i)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL113B)