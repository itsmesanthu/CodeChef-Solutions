# PYTHCL107

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### While Loop

Listen

LOOPS can execute a block of code as long as a specified condition is reached.
They are handy because they save time, reduce errors, and they make code more readable.

The WHILE LOOP loops through a block of code as long as a specified condition is true:

```
while (condition):
    // code to be executed

```

Example

```
counter = 0
while counter < 5:
    print("The counter is:", counter)
    counter = counter + 1

```

In the example above, the WHILE loop is executed as long as the condition `'counter < 5'` is true.
The initial value of `'counter'` is 0.
The code block inside the loop prints the value of Counter and increments it by 1 with the statement Counter = Counter + 1.
The loop will continue executing until `'counter'` becomes equal to or greater than 5.

### Task

Write a program which does the following

- Declare a variable a and initialize it to 0
- Use the syntax above to create a loop, output the following to the console Print the variable a in separate lines as long as it is less than 7. Don't print any other text. Increment a by 1 in each iteration.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-07T13:56:04.501Z  

```py
# Update the code below this line

a = 0
while a<7:
    print(a)
    a+=1
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL107)