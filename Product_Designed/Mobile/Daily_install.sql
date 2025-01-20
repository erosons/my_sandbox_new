SELECT install_date, COUNT(user_id) as total_installs
FROM mobile_downloads
WHERE install_date BETWEEN CURRENT_DATE - INTERVAL '30' DAY AND CURRENT_DATE
GROUP BY install_date
ORDER BY install_date;
--Segment data by day to count the number of new installs per day over the last 30 days.