{# Churn Rate Calculation

    Identify users who uninstall or stop using the app within the 30-day period.

Churn Rate Formula:
Churn Rate=(Uninstalled Users on Day N/Total Users Installed on Day N)×100 #}


SELECT install_date, COUNT(user_id) as churned_users
FROM mobile_downloads
WHERE uninstall_date IS NOT NULL
GROUP BY install_date;
