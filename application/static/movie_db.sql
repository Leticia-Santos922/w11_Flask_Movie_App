CREATE DATABASE movies_db; 

USE movies_db; 

CREATE TABLE movies(
  movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    year INT,
    duration VARCHAR(20)
);

INSERT INTO movies (title, genre, year, duration) 
VALUES
('Banal & Adama', 'Drama', 2023, '1hr 27m'),
('Alien', 'Sci-Fi', 1979, '1hr 57m'),
('The Boy and the Heron', 'Animation', 2023, '2hr 4m'),
('They Cloned Tyrone', 'Comedy', 2023, '2h 2m'),
('Past Lives', 'Romance', 2023, '1hr 45m'),
('Poor Things', 'Drama', 2023, '2hr 21m'),
('Taylor Swift: The Eras Tour', 'Documentary', 2023, '2hr 49m'),
('Thor: Ragnarok', 'Action', 2017, '2hr 10m'),
('Secret & Lies', 'Comedy', 1996, '2hr 16m'),
('Iron Man', 'Action', 2008, '2hr 6m');

SELECT * FROM movies;
