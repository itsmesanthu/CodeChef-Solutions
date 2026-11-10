# LEARNJSP129C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** JavaScript  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-10T16:24:35.404Z  

```js
// Submit the code and observe the flow

function greet(name, callback) {
  console.log("hello", name);
  
  // Calling back the callback function
  callback();
}

// Callback function
function sayGoodbye() {
  console.log('Goodbye!');
}

// Using the main function with a callback
greet('Alice', sayGoodbye);
```

---

[View on CodeChef](https://www.codechef.com/problems/LEARNJSP129C)