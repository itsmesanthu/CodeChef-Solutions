# PYTHCL113C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Single range argument

Listen

You can also pass just one argument to the range function.
When you use one argument in the range(n) function, it generates a sequence of numbers starting from 0 up to, but not including `N`.

```
for i in range(5):
    print(i)

```

Expected output:

```
0
1
2
3
4
# The sequence starts at 0 and ends at n-1. In this example, it generates numbers from 0 to 4.

```

So, the above loop runs 5 times. The `range(5)` function generates the numbers 0, 1, 2, 3, and 4.
This is useful when you need to repeat something a specific number of times.

### Task

Write a for loop that iterates 10 times (from 0 to 9) and prints the square of each number.

```
0
1
4
9
.
.
. 
81

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T15:56:42.728Z  

```py
# Update your code below this line
for i in range(0,10,1):
    print(i*i)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL113C)