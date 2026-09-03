# GSQ26

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Practice - Filter with multiple Like patterns

Listen

Let us now solve a practice problem which tests what we learnt in this sub-module -  **AND, OR & LIKE**.

You need to write a query with the following conditions

- Destination city end in 'o' AND
- Origin city starts with 'M'

```
Expected Output
Flights
┌──────────────┬────────────────┬────────┬────────┬─────────────┐
│ Passenger_id │ Passenger_name │ Gender │ Origin │ Destination │
├──────────────┼────────────────┼────────┼────────┼─────────────┤
│ 10004        │ Anthony        │ Male   │ Mumbai │ Cairo       │
└──────────────┴────────────────┴────────┴────────┴─────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T14:12:33.258Z  

```sql
/* write a query with the following conditions
- Destination city end in 'o' AND
- Origin city starts with 'M' 
*/
select * from Flights
where Destination like '%o' and Origin like 'M%';
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ26)