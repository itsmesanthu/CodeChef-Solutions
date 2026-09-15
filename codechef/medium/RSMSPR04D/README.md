# RSMSPR04D

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-4 Data Modification (Update and Alter)

Listen

Write queries for the following data modification operations based on the tables that we created and the data that we inserted.

### Task

Add a new column called "new_address" to the Customers table.
Set its default value to "Unknown".
Then, retrieve the name, address and new_address of the first customer from the Customers table.

### Expected output

```
┌──────────┬─────────────┬─────────────┐
│   name   │   address   │ new_address │
├──────────┼─────────────┼─────────────┤
│ John Doe │ 123 Main St │ Unknown     │
└──────────┴─────────────┴─────────────┘

```

### Tables
- Customers

```
┌─────────────┬─────────────┬──────────────────────┬────────────┬─────────────┐
│ customer_id │    name     │        email         │   phone    │   address   │
└─────────────┼─────────────┼──────────────────────┼────────────┼─────────────┘

```

- Products

```
┌────────────┬────────────────────┬─────────────┬────────┬────────────────┐
│ product_id │        name        │  category   │ price  │ stock_quantity │
└────────────┴────────────────────┴─────────────┴────────┴────────────────┘

```

- Orders

```
┌──────────┬─────────────┬────────────┬──────────────┬─────────────────┐
│ order_id │ customer_id │ order_date │ total_amount │ Remarks_if_any  │
└──────────┴─────────────┴────────────┴──────────────┴─────────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T16:02:06.226Z  

```sql
/* Update your query here*/
ALTER TABLE Customers 
ADD new_address VARCHAR(255) DEFAULT 'Unknown';
select name,address,new_address from Customers limit 1;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR04D)