-- Lists all the cities in hbtn_0d_usa using JOIN 
-- the database hbtn_0d_usa
SELECT cities.id, cities.name, state.name
FROM 'cities'
LEFT JOIN states
ON cities.state_id = states.id;
