
{# Group users by the day they installed the app (cohort) and track their retention on subsequent days.

Example SQL Query for Cohort Analysis: #}


SELECT install_date, active_date, COUNT(user_id) as active_users
FROM mobile_downloads
WHERE install_date BETWEEN CURRENT_DATE - INTERVAL '30' DAY AND CURRENT_DATE
GROUP BY install_date, active_date;
