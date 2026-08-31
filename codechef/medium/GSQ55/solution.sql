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