# GSQ11

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-31T09:44:11.946Z  

```sql
/* Write a query which does the following
- Add a new column 'Hourly_Pay' to the table employee and set the value as 100 by default.
- Output the entire table
*/
alter table employee 
add Hourly_Pay  default 100;
select * from employee;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ11)