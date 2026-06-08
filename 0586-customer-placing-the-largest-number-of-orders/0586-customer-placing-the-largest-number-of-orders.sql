# Write your MySQL query statement below
SELECT customer_number FROM(
SELECT COUNT(*) as count_number, customer_number
FROM Orders
GROUP BY customer_number
ORDER BY count_number DESC
LIMIT 1) tmp