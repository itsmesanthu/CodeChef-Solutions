/* Update your query here*/
ALTER TABLE Customers 
ADD new_address VARCHAR(255) DEFAULT 'Unknown';
select name,address,new_address from Customers limit 1;