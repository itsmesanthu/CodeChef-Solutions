# PYTHCL113A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Range of numbers

Listen

In Python, you can use a for loop to iterate over a sequence of numbers.
The Range() function helps generate this sequence, allowing you to define where to start, where to stop, and how much to increment by.

The basic syntax for using the Range() function in a for loop is:

```
for i in range(start, stop, step):
    # do something

```

 **How It Works** : When you provide three arguments to `range(start, stop, step)`, it generates numbers starting from start, up to (but not including) stop, incrementing by step.

For example:

```
for i in range(0, 10, 2):
    print(i)

```

Gives the Output:

```
0
2
4
6
8
# Let's see what's happening in the example given above:
# Start: The first number in the sequence. In range(0, 10, 2), the sequence starts at 0.
# Stop: The number where the sequence ends, but it is not included in the sequence. In range(0, 10, 2), the sequence stops before 10.
# Step: The difference between each number in the sequence. In range(0, 10, 2), the sequence increments by 2, generating numbers 0, 2, 4, 6, 8.

```

### Task
- Write a program to print integers from 55 to 100 with increments of 3. i.e, 55 58 61 64...so on till 100 (Excluding 100)

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T15:49:01.284Z  

```py
# Update the '_' to solve the problem
for i in range(55, 100,3):
    print(i)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL113A)