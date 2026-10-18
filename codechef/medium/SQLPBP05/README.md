# SQLPBP05

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-18T13:07:10.996Z  

```sql
-- your code goes here
select player_name,score from players where player_name in (select winner from matches) order by score desc ;
```

---

[View on CodeChef](https://www.codechef.com/problems/SQLPBP05)