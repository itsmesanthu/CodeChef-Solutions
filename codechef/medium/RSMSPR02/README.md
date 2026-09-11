# RSMSPR02

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T13:23:41.048Z  

```sql
/* Update the '_' in the code below */

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEST CHECK (category IN ('Electronics', 'Clothing', 'Grocery', 'Furniture')),
    price REAL NOT NULL CHECK (price > 0),
    stock_quantity INt CHECK (stock_quantity >=0)
);

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT UNIQUE NOT NULL,
    address TEXT DEFAULT 'Not Provided'
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount REAL CHECK (total_amount > 0),
    Remarks_if_any TEXT DEFAULT 'No Remarks'
);

```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR02)