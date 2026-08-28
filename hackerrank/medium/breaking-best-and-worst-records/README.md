# Between Two Sets

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Maria plays college basketball and wants to go pro.  Each season she maintains a record of her play.  She tabulates the number of times she breaks her season record for *most points* and *least points* in a game.  Points scored in the first game establish her record for the season, and she begins counting from there.

**Example**  
$scores = [12, 24, 10, 24]$   

Scores are in the same order as the games played.  She tabulates her results as follows:

<pre>
									 Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1
</pre>

Given the scores for a season, determine the number of times Maria breaks her records for *most* and *least* points scored during the season.

**Function Description**  

Complete the *breakingRecords* function in the editor below. 

breakingRecords has the following parameter(s):  

- *int scores[n]:* points scored per game   

**Returns**   

- *int[2]:* An array with the numbers of times she broke her records. Index $0$ is for breaking *most points* records, and index $1$ is for breaking *least points* records.  

**Input Format**

The first line contains an integer $n$, the number of games.  		
The second line contains $n$ space-separated integers describing the respective values of $score_0, score_1, \ldots, score_{n-1}$.

**Constraints**

* $1 \le n \le 1000$
* $0 \le scores[i] \le 10^8$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T13:12:35.962Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    count = 0
    for x in range(1, 101):
        if all(x % num == 0 for num in a):
            if all(num % x == 0 for num in b):
                count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem)