from sqlalchemy.sql import func
from flask_admin.contrib.sqla import ModelView

from project import db, admin


class Movies(db.Model):

    __tablename__ = 'moviesdb'

    mid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    # year = db.Column(db.String(4))
    rating = db.Column(db.Integer)

    def __repr__(self):
        return self.title


admin.add_view(ModelView(Movies, db.session))
