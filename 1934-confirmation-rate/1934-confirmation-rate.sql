# Write your MySQL query statement below
SELECT 
 S.user_id,
 ROUND(IFNULL(SUM(CASE WHEN C.action = "confirmed" THEN 1 ELSE 0 END) / COUNT(C.action) ,0), 2)
  AS confirmation_rate
FROM Signups S
LEFT JOIN Confirmations C
ON C.user_id = S.user_id
GROUP BY S.user_id
