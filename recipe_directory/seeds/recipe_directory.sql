DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY, 
    name text,
    cooking_time int,
    rating int
);

INSERT INTO recipes (name, cooking_time, rating) VALUES ('Cake', '30','3');
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Bread', '60','4');
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Fish', '60','2');
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Potatos', '20','2');
