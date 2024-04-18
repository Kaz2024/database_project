CREATE TABLE movies (
    id SERIAL PRIMARY KEY, 
    title text,
    genre text,
    release_year int
);
INSERT INTO movies (title, genre, release_year) VALUES ('Men in Black', 'Science Fiction','1997')
INSERT INTO movies (title, genre, release_year) VALUES ('Men in Black', 'Science Fiction','1997')