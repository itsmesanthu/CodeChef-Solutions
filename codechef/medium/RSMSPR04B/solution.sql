ALTER TABLE Orders 
ADD discount float(10, 2) DEFAULT 0.0;
select order_id,total_amount,discount from orders limit 1;