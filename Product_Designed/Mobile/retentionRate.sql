SELECT install_date, COUNT(user_id) as retained_users
FROM mobile_downloads
WHERE active_date = install_date + INTERVAL '1' DAY
GROUP BY install_date;
--Calculate how many users returned on specific days (e.g., Day 1, Day 7, Day 30).