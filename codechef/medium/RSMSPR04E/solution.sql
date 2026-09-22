ALTER TABLE Orders 
ADD discount DECIMAL(10, 4) DEFAULT 0;

UPDATE Orders 
SET discount = total_amount * 0.05 
WHERE total_amount > 900;

SELECT order_id, total_amount, discount 
FROM Orders 
WHERE discount > 0;