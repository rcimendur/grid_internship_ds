# Write your MySQL query statement below
with blabla as (
    select product_id, year as first_year, quantity, price,
    dense_rank() over (partition by product_id order by year asc) as drnk
    from Sales
)
select product_id, first_year, quantity, price
from blabla
where drnk = 1 