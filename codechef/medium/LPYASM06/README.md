# LPYASM06

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a list `colors` containing the items  **`['red', 'green', 'blue']`**.

You need to take two inputs from the user:

- The 1st line is the index number $n$ (assume 0-based indexing)
- The 2nd line has a string variable that represents a color

You need to insert  **`color`**  at  **index n**.

Output the new list after insertion. Check sample input / output below for further clarity.

### Sample 1:
Input
Output

```
0
black
```

```
['black', 'red', 'green', 'blue']
```

### Explanation:

The new items black will be inserted at index 0

### Sample 2:
Input
Output

```
3
purple
```

```
['red', 'green', 'blue', 'purple']
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T15:56:24.920Z  

```py
# Update the code below to solve the problem

colors = ['red', 'green', 'blue']
p=int(input())
w=input()
colors.insert(p,w)
print(colors)
    # TODO: write code...
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYASM06)