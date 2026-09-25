# PYTH73

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Conditions in if statements

Listen

You are given a score that the player has achieved in a 100 point game.

### Task

Print some text based on below conditions:

- If the score is 100, print "Perfect score"
- If the score is less than 100, but greater or equal to 80, print "Almost perfect score"
- If the score is less than 80, print "Nice try"
### Sample 1:
Input
Output

```
100
```

```
Perfect score
```

### Sample 2:
Input
Output

```
85
```

```
Almost perfect score
```

### Sample 3:
Input
Output

```
60
```

```
Nice try
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T13:45:44.751Z  

```py
score = int(input())
if score==100:
    print("Perfect score")
elif score>=80:
    print("Almost perfect score")
else:
    print("Nice try")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTH73)