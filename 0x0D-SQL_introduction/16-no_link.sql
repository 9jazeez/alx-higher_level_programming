-- This displays all records in second_table except those without
-- names from the given mysql server
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;
