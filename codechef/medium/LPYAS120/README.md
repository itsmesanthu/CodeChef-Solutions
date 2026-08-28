# LPYAS120

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to generate and print the  **Fibonacci series**  up to the  **$N$th term**  using a for-loop.

The  **Fibonacci series**  is the sequence where each number is the  **sum of the previous two numbers of the sequence** 

The number at the  **nth position**  can be represented by:
 **Fn = Fn-1 + Fn-2** 
where,
 **F0 = 0 and F1 = 1** 

Check the sample input / output below for further clarity.

### Sample 1:
Input
Output

```
10
```

```
0 1 1 2 3 5 8 13 21 34 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T12:19:46.995Z  

```py
n = int(input())
i=1
n1,n2=0,1
while i<=n:
    temp=n1+n2
    print(n1,end=" ")
    n1=n2
    n2=temp
    i+=1
    
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS120)