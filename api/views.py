from flask import Blueprint, jsonify, request
from . import db
from .models import Movies

main = Blueprint('main', __name__)


@main.route('/add_movie', methods=['POST'])
def add_movie():

    movie_data = request.get_json()

    title = movie_data['title']
    rating = movie_data['rating']

    new_movie = Movies(title=title, rating=rating)
    db.session.add(new_movie)
    db.session.commit()

    return 'Done', 201


@main.route('/movies')
def movies():

    movies_list = [{'title': movie.title, 'rating': movie.rating}
                   for movie in Movies.query.all()]

    print(movies_list)

    return jsonify({'movies': movies_list})
