from flask.cli import FlaskGroup

from project import create_app, db
from project.api.movies.models import Movies


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Movies(title="Iron Man", rating=5))
    db.session.add(Movies(title="Exmachina", rating=4))
    db.sess.commit()


if __name__ == '__main__':
    cli()