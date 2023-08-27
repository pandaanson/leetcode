# Write your MySQL query statement below
SELECT 
    s1.start_day,
    MIN(t1.end_day) AS end_day,
    s1.hall_id
FROM HallEvents s1 
-- Join the table with itself to compare events of the same hall
INNER JOIN HallEvents t1 ON s1.start_day <= t1.end_day AND s1.hall_id = t1.hall_id
-- Exclude rows where there exists another event that overlaps with the end date of t1 but ends later
AND NOT EXISTS(
    SELECT * FROM HallEvents t2 
    WHERE t1.end_day >= t2.start_day AND t1.end_day < t2.end_day AND s1.hall_id = t2.hall_id
)
-- Exclude rows where there exists another event that starts before and ends after or at the start date of s1
WHERE NOT EXISTS(
    SELECT * FROM HallEvents s2 
    WHERE s1.start_day > s2.start_day AND s1.start_day <= s2.end_day AND s1.hall_id = s2.hall_id
)
-- Group by the start day and hall_id to find the minimum end day
GROUP BY s1.start_day, s1.hall_id
-- Order the results
ORDER BY s1.hall_id, s1.start_day
