# Write your MySQL query statement below
with rankedsals as (
    select d.name as Department, e.name as Employee, e.salary as Salary,
    dense_rank() over (partition by e.departmentId order by e.salary desc) as drnk
    from Employee e join Department d on e.departmentId = d.id
)
select Department, Employee, Salary
from rankedsals
where drnk <= 3