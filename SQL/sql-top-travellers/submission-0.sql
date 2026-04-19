-- Write your query below
select u.name, COALESCE(s.full_distance, 0) as travelled_distance from users u
left join (select user_id, sum(distance) as full_distance from rides group by user_id) s 
on s.user_id = u.id
order by travelled_distance desc, u.name