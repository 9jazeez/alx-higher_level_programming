-- List all the genres without yhe genre comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN ( SELECT a.title FROM tv_shows AS a
	                     JOIN tv_show_genres as b
			     ON a.id = b.show_id
			     JOIN tv_genres AS c
			     ON b.genre_id =  c.id
			     WHERE c.name = 'Comedy')
ORDER BY tv_shows.title ASC;
