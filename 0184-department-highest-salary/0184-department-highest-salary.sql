# Write your MySQL query statement below
SELECT D.name as Department, E.name as Employee, E.salary as Salary
FROM Employee as E
JOIN (SELECT departmentId, MAX(salary) as max_salary
    FROM Employee
    GROUP BY departmentId
) as M
ON E.departmentId = M.departmentId
JOIN Department D
ON E.departmentId = D.id
WHERE E.salary = M.max_salary
