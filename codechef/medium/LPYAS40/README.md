# LPYAS40

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to print the length of each word of the sentence given below as well as the length of the whole sentence.
 **"Coding on CodeChef"** 

#### Note:

There is spacing between the words and the number, consider it while printing the outputs.

 **Note:**  Please print the outputs in the same format as given below.

### Output Format

Coding - 6
on - 2
CodeChef - 8
Coding on CodeChef - 18

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-30T12:42:00.248Z  

```py
s="Coding on CodeChef"
w=s.split()
for i in w:
    print(i,"-",len(i))
print(f"{s} - {len(s)}")
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS40)