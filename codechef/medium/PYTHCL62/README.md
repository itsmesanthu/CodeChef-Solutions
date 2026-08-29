# PYTHCL62

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### If & Else Statements

Listen

We use conditions in code for decision making and controlling the flow of a program.

 **IF**  and  **ELSE**  can be used together to create conditions. The syntax for this is:

```
if condition:
    # code to run if the condition is true
else:
    # code to run if the above condition is false

```

Condition can be any expression which you are trying to evaluate. A simple condition can be:

```
a = 4
b = 5
if a == b:
    print("a and b are equal")
else:
    print("a and b are not equal")

# Output:
# a and b are not equal
#`a == b` is used to check whether the values of variables `a` and `b` are equal. `==` is called a equal to operator.

```

Here's a table of common operators used in Python conditions:

Operator	Description	Example
`==`	Equal to	`a == b`
`!=`	Not equal to	`a != b`
`>`	Greater than	`a > b`
`<`	Less than	`a < b`
`>=`	Greater than or equal to	`a >= b`
`<=`	Less than or equal to	`a <= b`
### Task

Write a program which does the following

- Let's think of a real-life example where we need to find out if a person is old enough to vote.
- Find out if the age entered by the user is greater than OR equal to the voting age limit, which is set to 18.
- Declare the variable age - take an integer input and store it in age.
- Compare age and voting age limit using the syntax given above and output the following "Old enough to vote" if age is greater than or equal to voting age limit "Not old enough to vote" if age is lesser than voting age limit
### Sample 1:
Input
Output

```
20
```

```
Old enough to vote
```

### Sample 2:
Input
Output

```
15
```

```
Not old enough to vote
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T13:09:10.350Z  

```py
# Update the '_' in the code below to solve the problem

age =int(input())

if age>=18:
    print("Old enough to vote")
else:
    print("Not old enough to vote")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL62)