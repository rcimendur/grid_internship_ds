# Write your MySQL query statement below
with firstLogin as
(
    select player_id, event_date, 
    min(event_date) over (partition by player_id) as first_login
    from Activity
)
select round(
    count(distinct case when datediff(event_date, first_login) = 1 then player_id end) / 
    count(distinct player_id),
     2
     ) as fraction
    from firstLogin

