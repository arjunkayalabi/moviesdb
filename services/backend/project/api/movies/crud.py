from project import db
from project.api.movies.models import Movies


def get_all_users():
    return Movies.query.all()


def get_movie_by_id(movie_id):
    return Movies.query.filter_by(mid=movie_id).first()


def get_movie_by_title(title):
    return Movies.query.filter_by(title=title).first()


def add_movie(title, rating):
    movie = Movies(title=title, rating=rating)
    db.session.add(movie)
    db.session.commit()
    return movie


def update_movie(movie, title, rating):
    movie.title = title
    movie.rating = rating
    db.session.commit()
    return movie


def delete_movie(movie):
    db.session.delete(movie)
    db.session.commit()
    return movie
