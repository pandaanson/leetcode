WITH AllUsers AS (
  SELECT DISTINCT user1 AS user FROM Friends
  UNION
  SELECT DISTINCT user2 AS user FROM Friends
),
UniqueFriendCounts AS (
  SELECT 
    user,
    COUNT(DISTINCT friend) AS friend_count
  FROM (
    SELECT user1 AS user, user2 AS friend FROM Friends
    UNION ALL
    SELECT user2 AS user, user1 AS friend FROM Friends
  ) AS UnifiedFriends
  GROUP BY user
),
TotalUsers AS (
  SELECT COUNT(*) AS total_users FROM AllUsers
)
SELECT 
  ufc.user AS user1,
  ROUND((ufc.friend_count / TotalUsers.total_users) * 100, 2) AS percentage_popularity
FROM 
  UniqueFriendCounts ufc, TotalUsers
ORDER BY 
  ufc.user;
