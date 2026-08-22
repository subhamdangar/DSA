# Write your MySQL query statement below

SELECT name as Customers
FROM Customers
LEFT OUTER JOIN Orders
ON Customers.id = Orders.customerId
WHERE customerId is NULL;