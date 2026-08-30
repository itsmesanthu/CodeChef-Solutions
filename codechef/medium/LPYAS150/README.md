# LPYAS150

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program that first accepts the number of test cases  **t**. For each test case, read an integer  **num**. Check if  **num**  is even using the  **isEven**  function. If  **num**  is even, output "Even"; otherwise, output "Odd".

### Sample 1:
Input
Output

```
3
2
6
5
```

```
Even
Even
Odd
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-30T13:08:10.373Z  

```py
def is_even(num):
    if num%2==0:
        return True
    else:
        return False

def main():
    t=int(input())
    for i in range(t):
        num=int(input())
        if is_even(num):
            print("Even")
        else:
            print("Odd")
if __name__ == "__main__":
    main()

```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS150)