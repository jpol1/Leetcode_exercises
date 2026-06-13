# Write your MySQL query statement below
SELECT P.project_id, ROUND(SUM(E.experience_years) / COUNT(E.experience_years),2) as average_years
FROM Project P
JOIN Employee E
ON E.employee_id = P.employee_id
GROUP BY P.project_id