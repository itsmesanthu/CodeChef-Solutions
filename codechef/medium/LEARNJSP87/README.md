# LEARNJSP87

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Incorrect Conditionals

Listen

Incorrect conditionals are one of the most common types of logical errors. They occur when you put an incorrect condition in if-else.

### Example

The code below is supposed to do the following

- If an integer is even, then output even
- If an integer is odd, then output odd

```
var n = 10;

if (n % 2 === 0) {
    console.log("odd");
} else {
    console.log("even");
}

```

The above code is incorrect because it outputs `odd` when the number is even. Changing the `if` condition will fix the error.

```
var n = 10;

if (n % 2 != 0) {
    console.log("odd");
else {
    console.log("even");
}

```

### Task

Given function checks whether a number is greater than 5 or not.

- Run the code without changing anything, it will give a wrong answer.
- Find the wrong condition and correct it.
### Sample 1:
Input
Output

```
5
```

```
the number is smaller than or equal to 5
```

### Sample 2:
Input
Output

```
6
```

```
the number is greater than 5
```

## Solution

**Language:** JavaScript  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-16T09:06:32.037Z  

```js
// Fix the following function

function check(n) {
  if (n >5) {
    console.log("the number is greater than 5");
  } else {
    console.log("the number is smaller than or equal to 5");
  }
}

```

---

[View on CodeChef](https://www.codechef.com/problems/LEARNJSP87)