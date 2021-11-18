-- Uses the imported temperature table to display the averages
-- by city oredered by temp (descending order) for best 3
SELECT city AVG(value) AS avg_temp FROM temperatures WHERE montth >= 9 AND month < 9 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
