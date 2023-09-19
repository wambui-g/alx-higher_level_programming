-- lists all records of second_table 
-- displays the score and name 
-- lists in desc order

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
