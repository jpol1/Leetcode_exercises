# Write your MySQL query statement below
SELECT W.id
FROM Weather W
JOIN Weather W_D
ON W.recordDate = W_D.recordDate + INTERVAL 1 DAY
WHERE W.temperature > W_D.temperature