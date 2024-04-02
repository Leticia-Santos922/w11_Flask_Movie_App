from flask import render_template, request, url_for
from application import app
from data_access import get_random_movie


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html')


# decorator associates the function movies() with URL route and GET and POST requests
@app.route('/movie', methods=['GET', 'POST'])
def movie():
    # checks if current request method is post, if it is it means the user has submitted a form to this route
    if request.method == 'POST':
        # retrieves the value of the genre parameter from the form submitted
        genre = request.form.get('genre')
        # calls the get_random_movie function to the genre obtained from the form
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
