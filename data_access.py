import mysql.connector
import random


def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="movies_db"
    )


# defined function name which takes the parameter genre
def get_random_movie(genre):
    # established a connection to the database
    moviedb = get_database_connection()

    # more efficient code
    # mysql cursor is instantiating the mysql class
    cursor = moviedb.cursor()

    if genre:
        query = "SELECT * FROM movies WHERE genre = %s ORDER BY RAND() LIMIT 1"
        cursor.execute(query, (genre,))
    else:
        query = "SELECT * FROM movies ORDER BY RAND() LIMIT 1"
        cursor.execute(query)

        # Fetch one result
    random_movie = cursor.fetchone()

    return random_movie

