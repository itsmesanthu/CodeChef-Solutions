# RSMSPR03D

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-3D Data Retrieval Using Queries

Listen

Write queries for the following data retrieval operations based on the tables that we created and the data that we inserted.

### Task

Find customers who have not provided their address.

### Expected output

```
┌─────────────┬─────────────┬─────────────────────┬────────────┬──────────────┐
│ customer_id │    name     │        email        │   phone    │   address    │
├─────────────┼─────────────┼─────────────────────┼────────────┼──────────────┤
│ 5           │ Charlie Lee │ charlie.l@email.com │ 9234567890 │ Not Provided │
│ 7           │ Emily Clark │ emily.c@email.com   │ 9345678901 │ Not Provided │
└─────────────┴─────────────┴─────────────────────┴────────────┴──────────────┘

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
**Submitted:** 2026-09-11T13:40:35.997Z  

```sql
select * from customers where address='Not Provided';
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR03D)