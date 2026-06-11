# Write your MySQL query statement below
SELECT P.product_id, ROUND(IFNULL(SUM(P.price * U.units) / SUM(U.units),0), 2) as average_price
FROM Prices P
LEFT JOIN UnitsSold U
ON U.product_id = P.product_id
AND P.start_date <= U.purchase_date
AND U.purchase_date <= P.end_date
GROUP BY P.product_id