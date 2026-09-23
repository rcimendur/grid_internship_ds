# Write your MySQL query statement below
select firstname, lastname, city, state
from Person left join Address using(personId)