# LPYAS100B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to create a shopping list of `5` items and check if a given item exists in the list or not.

### Input Format
- The first line of input contains five space separated strings - the items of the shopping list.
- Next line contains a single string - the item which we need to check.
### Output Format
- Print on a single line YES if given item exists in the list, else print NO.
### Sample 1:
Input
Output

```
ToothBrush Pen NoteBook Pencil Chess
Ludo
```

```
NO
```

### Explanation:

Since the item `Ludo` doesn't exist in the shopping list, the output is  **NO**.

### Sample 2:
Input
Output

```
ToothBrush Pen NoteBook Pencil Chess
Pen
```

```
YES
```

### Explanation:

Since the item `Pen` exists in the shopping list, the output is  **YES**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T15:49:32.868Z  

```py
# Write your code below
s=input().split()
t=input()
if t in s:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS100B)