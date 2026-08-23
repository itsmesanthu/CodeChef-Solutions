# PYPRACMCQ9

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Is It Oneful Pair - MCQ

Chef defines a pair of positive integers $(a, b)$ to be a $\text{Oneful Pair}$, if

$a + b + (a \cdot b) = 111$

For example, $(1, 55)$ is a $\text{Oneful Pair}$, since $1 + 55 + (1 \cdot 55) = 56 + 55 = 111$.
But $(1, 56)$ is not a $\text{Oneful Pair}$, since $1 + 56 + (1 \cdot 56) = 57 + 56 = 113 \neq 111$.

Which of these pairs are $\text{Oneful Pair}$?

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-23T15:52:06.906Z  

```cpp
x,y = map(int,input().split())

if x>=2*y:
    print("YES")
else:
    print("NO")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYPRACMCQ9)