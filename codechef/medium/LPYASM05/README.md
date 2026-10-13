# LPYASM05

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a list of colors in the IDE.

You need to write a code that take the user input - an integer.
You need to pop the element at the position indicated by the integer.
Output the updated list once the element has been removed.
Check the sample input / output given below for clarity.

Note: Python lists are 0 indexed - however, the integer shows the position to be removed from the list.
Think about how this will change your code.

### Sample 1:
Input
Output

```
2
```

```
['black', 'white', 'cyan', 'yellow', 'green']
```

### Sample 2:
Input
Output

```
6
```

```
['black', 'blue', 'white', 'cyan', 'yellow']
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T15:52:56.221Z  

```py
# Update the code below to solve the problem

colors = ['black', 'blue', 'white', 'cyan', 'yellow', 'green']
p=int(input())
colors.pop(p-1)
print(colors)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYASM05)