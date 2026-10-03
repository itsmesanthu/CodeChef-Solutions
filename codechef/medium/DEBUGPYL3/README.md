# DEBUGPYL3

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Compilation error continued

Listen

How do you identify `Compilation error`?

When you run your code and there is an error, you will typically see it in the output.

For example if you run the below code, you will get a syntax error.

```
name = "piyush"
if name == "piyush"
    print(name)

```

 **Error** 

```
  File "/mnt/sol.py", line 2
    if name == "piyush"
                       ^
SyntaxError: expected ':'

# The error description says that there is a error on line 2. The exact error is explained on the last line of the description: `SyntaxError: expected ':'`.

```

It is clearly saying that a : (colon) is expected after the IF statement.
The error goes away after adding : (colon).

### Task
- Submit the code present in IDE as it is.
- Read the error statement and understand what needs to be fixed.
- Fix the code so that it correctly outputs: "Even".

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T16:35:51.908Z  

```py
age = 28
if age % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

[View on CodeChef](https://www.codechef.com/problems/DEBUGPYL3)