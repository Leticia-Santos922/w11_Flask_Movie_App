from flask import render_template, request, url_for
import random
from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About', favourites=['crocheting', 'reading'])


movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "year": 1994},
    {"title": "The Godfather", "genre": "Crime", "year": 1972},
    {"title": "The Dark Knight", "genre": "Action", "year": 2008},
    {"title": "Pulp Fiction", "genre": "Crime", "year": 1994},
    {"title": "Forrest Gump", "genre": "Drama", "year": 1994}
    # Add more movies as needed
]


@app.route('/movie', methods=['GET', 'POST'])
def movie():
    # pick a random movie
    if request.method == 'POST':
        # Pick a random movie
        movie = random.choice(movies)
        return render_template('movie.html', title='Movie', movies=movies, movie=movie)
    else:
        return render_template('movie.html', title='Movie', movies=movies)


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/login')
def login():
    return render_template('login.html', title='Register')
