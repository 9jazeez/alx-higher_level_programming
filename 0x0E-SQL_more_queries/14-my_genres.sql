-- All genres with the number of shows linked to them
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_genres.genre_id
JOIN tv_showws
ON tv_show_genres_show_id = tv_shows.id
WHERE tv_shows.tittle = "Dexter"
ORDER BY tv_genres.name;
