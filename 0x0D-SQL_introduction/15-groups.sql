-- List the score in second_table according to occurrence
-- from a table inside given mysql server
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
