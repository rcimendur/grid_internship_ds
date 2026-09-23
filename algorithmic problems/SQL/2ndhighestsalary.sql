with ranksalaries as (
    select salary, dense_rank() over (order by salary desc) as drnk from Employee
)
select (select salary from ranksalaries where drnk = 2 limit) as SecondHighestSalary