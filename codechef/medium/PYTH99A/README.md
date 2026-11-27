# PYTH99A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### For Loop

Listen

`For loop` can also be used to iterate over a string.

```
name = "Alice"
for char in name:
    print(char)

```

Here, the For loop iterates over each character in the `'name'` string.
The `'char'` variable takes on the value of each character, and it is printed.
The output will be:

```
A
l
i
c
e

```

### Task

Write a program which does the following:

- You are given a string containing some occurrences of the alphabet 'o'
- Count how many o's are present in the string using a 'for' loop and 'if' condition and print the count.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-27T15:47:36.840Z  

```py
# Count how many 'o's are present in the string using a 'for' loop and 'if' condition

string = 'bolloon'

# use this variable to count occurrences of o
count_o = 0      
for i in string:
    if i=="o":
        count_o+=1
print(count_o)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH99A)