-- Uses the imported temperature table to display the averages
-- by city oredered by temp (descending order)
SELECT city AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
