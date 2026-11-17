# LEARNJSP86

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Logical Error or Wrong Answer (WA)

Listen

A logical error is an error in a program that occurs when the code compiles and runs without producing any error messages, but it does not produce the expected or desired output.

Instead, it performs a different computation or provides incorrect results due to a flaw in the algorithm or logic of the program.

Logical errors are the hardest to find in a program. One needs to have enough debugging practice to figure out logical errors.

They can be categorized into different types:

- Incorrect Conditions
- Incorrect Index
- Incorrect variable usage

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-17T15:58:28.574Z  

```cpp
// Debug/Fix the given function

function solve(num1, num2) {
  var isEqual = "Equal";
  if(num1 === num2) {
     isEqual = "Equal";
  } else {
     isEqual = "Not Equal";
  }
  console.log(isEqual);
}
```

---

[View on CodeChef](https://www.codechef.com/problems/LEARNJSP86)