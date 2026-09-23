CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        with ranksalaries as (
            select salary, dense_rank() over (order by salary desc) as drnk
            from employee
        )
        select distinct salary
        from ranksalaries
        where drnk = N
  );
END