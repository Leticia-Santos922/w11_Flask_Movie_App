import mysql.connector
import random
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password",
#     database="movies_db"
# )


def get_random_movie(genre=None):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="movies_db"
    )
    # create cursor object - why is this important?
    cursor = mydb.cursor()

    # Execute query to fetch all movies from the database
    # Construct the SQL query
    if genre:
        query = "SELECT * FROM movies WHERE genre = %s"
        cursor.execute(query, (genre,))
    else:
        cursor.execute("SELECT * FROM movies")

    # Fetch all rows from the result set
    movies = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    mydb.close()

    # Pick a random movie from the list
    if movies:
        random_movie = random.sample(movies, 1)[0]  # Select a single random movie from the list
        return random_movie
    else:
        return None