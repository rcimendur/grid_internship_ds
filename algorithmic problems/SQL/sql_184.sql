# Write your MySQL query statement below
with depsalaries as (
    select d.name as Department, 
    e.name as Employee, 
    e.salary, 
    dense_rank() over (partition by e.departmentId 
                        order by e.salary desc) as drnk
    from Employee e join Department d ON e.departmentId = d.id
)
select Department, Employee, Salary
from depsalaries
WHERE drnk = 1