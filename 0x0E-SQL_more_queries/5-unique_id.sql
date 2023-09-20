-- creates table with id int, default 1 and unique, name VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256));
