from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from models import Movie
from form import RatingForm, TitleForm
from extensions import db
import requests


"""----------------------------APP CONFIG----------------------------"""

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
Bootstrap5(app)


"""----------------------------INIT DATA BASE----------------------------"""

db.init_app(app)

with app.app_context():
    db.create_all()


"""--------------------------------API CONFIGURATION----------------------------------------------"""

API_KEY = "94f41153697fc2dd06780bf4fe755830"
API_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
HEADERS = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5NGY0MTE1MzY5N2ZjMmRkMDY3ODBiZjRmZTc1NTgzMCIsInN1YiI6IjY1ZWM3NmJmOWQ4OTM5MDE0OTI5NmQ1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Idnqvh6AtCzcH_PIS4ZYeMMpxRgkX1JB-cyAr1uy7OA'
}

"""-------------------------------------APP ROUTES------------------------------------------------"""


@app.route("/")
def home():
    with app.app_context():
        all_movies = Movie.query.order_by(Movie.rating.desc()).all()

        for index, movie in enumerate(all_movies):
            movie.ranking = index + 1

    return render_template("index.html", all_movies=all_movies)


@app.route("/edit/<int:index>", methods=['POST', 'GET'])
def edit(index):
    form = RatingForm()

    with app.app_context():
        movie = db.get_or_404(Movie, index)

        if form.validate_on_submit():
            movie.rating = float(form.rating.data)
            movie.review = form.review.data

            db.session.commit()

            return redirect(url_for('home'))

    return render_template('edit.html', form=form, index=index, movie=movie)


@app.route("/delete/<int:index>")
def delete(index):
    with app.app_context():
        movie = db.get_or_404(Movie, index)

        db.session.delete(movie)
        db.session.commit()

    return redirect(url_for('home'))


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = TitleForm()

    if form.validate_on_submit():
        movie_title = form.title.data

        params = {
            'query': movie_title
        }

        data_movies = requests.get(url=API_ENDPOINT, headers=HEADERS, params=params).json()['results']

        return render_template("select.html", data_movies=data_movies)

    return render_template("add.html", form=form)


@app.route("/select/<int:index>")
def select(index):

    params = {
        'movie_id': index
    }

    movie = requests.get(url=f"https://api.themoviedb.org/3/movie/{index}?language=en-US", headers=HEADERS, params=params).json()

    with app.app_context():
        new_movie = Movie(title=movie['original_title'],
                          year=movie['release_date'].split("-")[0],
                          img_url='https://image.tmdb.org/t/p/w500/' + movie['poster_path'],
                          description=movie['overview'])

        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('edit', index=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
