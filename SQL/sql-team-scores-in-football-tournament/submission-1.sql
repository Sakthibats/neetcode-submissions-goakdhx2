select 
    t.team_id, 
    t.team_name, 
    COALESCE(SUM(
        CASE
            WHEN t.team_id = m.host_team AND m.host_goals > m.guest_goals THEN 3
            WHEN t.team_id = m.guest_team AND m.guest_goals > m.host_goals THEN 3
            WHEN m.host_goals = m.guest_goals THEN 1
            ELSE 0
        END
    ), 0) AS num_points
from teams t 
left join matches m on t.team_id = m.host_team or t.team_id = m.guest_team
group by t.team_id, t.team_name
order by num_points desc, t.team_id asc