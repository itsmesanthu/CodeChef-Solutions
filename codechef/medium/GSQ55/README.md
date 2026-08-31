# GSQ55

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Practice - Alter Table and Insert Data

Listen

Existing table - 'customer' with column headers and 0 rows.

```
┌────┬───────────────┬─────┬──────────┐
│ Id │     Name      │ Age │ Address  │
└────┴───────────────┴─────┴──────────┘

```

### Task

Write a query which does the following

- Take the table given above and add an additional column 'email' to the table 'customer'.
- Consider the table 'customer' to be empty and insert the below data
- Output all the entires in the table.
### Expected output

```
┌────┬───────────────┬─────┬──────────┬──────────────┐
│ Id │     Name      │ Age │ Address  │    email     │
├────┼───────────────┼─────┼──────────┼──────────────┤
│ 1  │ John Smith    │ 25  │ Main St  │ john@ex.com  │
│ 2  │ Sarah Johnson │ 30  │ Broadway │ sarah@ex.com │
└────┴───────────────┴─────┴──────────┴──────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-31T14:48:21.353Z  

```sql
/* Write a query to add an additional column 'email' to the table 'customer'.
Consider the table 'customer' to have Id, Name, Age, Address as existing columns*/

-- Alter the existing table to add the column 'email'
Alter table customer
add email text;

-- Insert into 'customer' all the values for the corresponding columns
insert into customer(Id,Name,Age,Address,email)

VALUES(1, 'John Smith', 25, 'Main St','john@ex.com'),
(2, 'Sarah Johnson', 30,'Broadway','sarah@ex.com');

-- Output the entire table to the console
select * from customer
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ55)