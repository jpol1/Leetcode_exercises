# Write your MySQL query statement below
SELECT A.machine_id, ROUND(AVG(A_D.timestamp-A.timestamp),3) as processing_time
FROM Activity A
JOIN Activity A_D
ON A.machine_id = A_D.machine_id
AND A.process_id = A_D.process_id
WHERE A.activity_type = 'start' 
AND A_D.activity_type = 'end'
GROUP BY A.machine_id;
