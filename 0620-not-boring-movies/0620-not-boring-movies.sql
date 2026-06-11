# Write your MySQL query statement below
SELECT *
FROM Cinema C
WHERE C.description != 'boring' AND (C.id % 2 !=0)
ORDER BY C.rating DESC