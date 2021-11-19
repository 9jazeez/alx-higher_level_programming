-- All genres with the number of shows linked to them
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres_show_id = tv_shows.id
JOIN tv_showws
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.name = "Comedy"
ORDER BY tv_genres.title;
