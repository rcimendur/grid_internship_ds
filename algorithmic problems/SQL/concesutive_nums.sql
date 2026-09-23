# Write your MySQL query statement below
with consecLog as (
    select num, 
    lag(num) over (order by id) as prev1, 
    lag(num, 2) over (order by id) as prev2
    from Logs
)
select distinct num as ConsecutiveNums from consecLog where num = prev1 and num = prev2