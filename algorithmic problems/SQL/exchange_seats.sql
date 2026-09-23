# Write your MySQL query statement below
select id, COALESCE(
    CASE 
        WHEN id % 2 = 1 then lead(student) over (order by id) 
        ELSE lag(student) over (order by id) END, student) as student
from Seat
order by id