# Write your MySQL query statement below
with emailcounter as (
    select email, count(email) as cnt
    from person
    group by email
)
select email as Email from emailcounter where cnt > 1