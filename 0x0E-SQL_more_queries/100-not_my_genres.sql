-- List all the genres not linked to Dexteer
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN ( SELECT a.name AS naame FROM tv_genres AS a
	                     JOIN tv_show_genres as b
			     ON b.genre_id = a.id
			     JOIN tv_shows AS c
			     ON b.show_id c.id
			     WHERE c.title = 'Dexter')
ORDER BY tv_genres.name ASC;
