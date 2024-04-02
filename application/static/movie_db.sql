CREATE DATABASE movies_db; 

USE movies_db; 

CREATE TABLE movies(
  movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
	movie_image VARCHAR(100), 
    genre VARCHAR(50) NOT NULL,
    year INT,
    duration VARCHAR(20)
);

INSERT INTO movies (title, movie_image, genre, year, duration) 
VALUES
('Banal & Adama', 'images/banalandadama.jpg',  'Drama', 2023, '1hr 27m'),
('Alien', 'images/alien.jpg','Sci-Fi', 1979, '1hr 57m'),
('The Boy and the Heron', 'images/boyandheron.jpg', 'Animation', 2023, '2hr 4m'),
('They Cloned Tyrone', 'images/clonecalledtyrone.jpg','Comedy', 2023, '2h 2m'),
('Past Lives', 'images/pastlives.jpg', 'Romance', 2023, '1hr 45m'),
('Poor Things', 'images/poorthing.jpg','Drama', 2023, '2hr 21m'),
('Taylor Swift: The Eras Tour', 'images/taylorswift.jpg', 'Documentary', 2023, '2hr 49m'),
('Thor: Ragnarok', 'images/thor.jpg', 'Action', 2017, '2hr 10m'),
('Secret & Lies', 'images/secretsandlies.jpg', 'Comedy', 1996, '2hr 16m'),
('Iron Man', 'images/ironman.jpg', 'Action', 2008, '2hr 6m');

SELECT * FROM movies;
