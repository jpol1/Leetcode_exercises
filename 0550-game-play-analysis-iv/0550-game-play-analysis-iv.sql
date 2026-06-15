# Write your MySQL query statement below
SELECT
    ROUND(COUNT(DISTINCT A.player_id) / COUNT(DISTINCT F.player_id),2)
    as fraction
FROM (
    SELECT player_id, MIN(event_date) as first_login
    FROM Activity
    GROUP BY player_id
) F
LEFT JOIN Activity A
ON A.player_id = F.player_id
AND A.event_date = F.first_login + INTERVAL 1 DAY
