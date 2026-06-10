# Write your MySQL query statement below
SELECT V.customer_id, COUNT(*) as count_no_trans
FROM Transactions T
RIGHT JOIN Visits V
ON V.visit_id = T.visit_id
WHERE T.transaction_id IS NULL
GROUP BY V.customer_id
