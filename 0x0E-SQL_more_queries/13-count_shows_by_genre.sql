-- All genres with the number of shows linked to them
SELECT g. 'name' AS 'genre', COUNT(*) AS 'number_of_shows'
FROM 'tv_genre' AS g
	INNER JOIN 'tv_show_genre' AS t
	ON g. id = t.'genre_id'
GROUP BY g.'naame'
ORDER BY 'number_of_shows' DESC;
