/* Write a query which does the following */

-- Create a table 'customer'
Create table customer(
Id integer primary key,
Name text not null,
Age integer not null,
address text not null);

-- Insert data into the table 
Insert Into customer(Id,Name,Age,address)
VALUES(1, 'John Smith', 25,  '123 Main St'),
(2, 'Sarah Johnson', 30,'456 Broadway'),
(3, 'Michael Brown', 45, '789 5th Ave'),
(4, 'Jessica Davis', 28, '321 Elm St'),
(5, 'David Lee', 35,  '555 Park Ave');

-- Output the entire table
select * from customer;