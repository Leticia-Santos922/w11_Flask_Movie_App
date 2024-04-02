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

    # mysql cursor is instantiating the mysql class
    cursor = moviedb.cursor()
    # Execute query to fetch all movies from the database
    # Construct the SQL query
    if genre:
        query = "SELECT * FROM movies WHERE genre = %s"
        # execute is passing through the query above: the %s is the parameters and placeholder to pass through any values in
        # %s which is the genres "Animation, Drama"
        # genre is a tuple because it does not change and same placeholder
        cursor.execute(query, (genre,))
    else:
        # anything that is not a genre executes this query
        cursor.execute("SELECT * FROM movies")

    # Fetch all rows from the result set
    movies = cursor.fetchall()
    # todo: is it good practice to close the connection and what does this mean?
    # Close cursor and connection
    # cursor.close()
    # moviedb.close()
    # Pick a random movie from the list
    if movies:
        random_movie = random.sample(movies, 1)[0]  # Select a single random movie from the list
        return random_movie
    else:
        return None
