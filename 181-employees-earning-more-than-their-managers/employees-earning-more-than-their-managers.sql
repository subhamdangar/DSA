# Write your MySQL query statement below

select m.name as Employee from Employee as e INNER JOIN Employee as m on e.id = m.managerId where e.salary < m.salary;