-- lists all cities in Carlifonia found in database

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDERED BY id;
