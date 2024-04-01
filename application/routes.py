from flask import render_template, request, url_for
from application import app
from data_access import get_random_movie


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/movie', methods=['GET', 'POST'])
def movie():
    # pick a random movie
    if request.method == 'POST':
        # Check if the form contains the genre parameter
        genre = request.form.get('genre')
        # Pick a random movie
        movie = get_random_movie(genre)
        return render_template('movie.html', title='Movie', movie=movie)
    else:
        return render_template('movie.html', title='Movie')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/login')
def login():
    return render_template('login.html', title='Register')
