# PYTH99

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### For Loop

Listen

When you know exactly how many times you want to loop through a block of code, use the for loop instead of while loop.
FOR loop in Python is designed to iterate over a sequence of elements, such as a list, string, or range of numbers.

Example 1: Iterating over a list

```
fruits = ["apple", "banana", "orange"]
for item in fruits:
    print(item)

```

The For loop iterates over each element in the  **`fruits`**  list.
On each iteration, the  **`item`**  variable takes the value of the current element, and it is printed.
The output will be:

```
apple
banana
orange

```

 **Note:** 

- There was no increment in the For loop syntax. Unlike While loop - we did not need to write 'item = item + 1' or any such syntax
- item is just a Variable. You can replace it with element / i / x or any other Variable.
### Task

Write a program which does the following

- You are given a list of numbers
- Print each item of the list on a separate line

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T15:28:18.288Z  

```py
# Print each item of the list on a separate line

numbers = [1, 6, 4, 3, 2, 5]
for i in numbers:
    print(i)
    
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH99)