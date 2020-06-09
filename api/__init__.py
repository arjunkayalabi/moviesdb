from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_admin import Admin
from flask_migrate import Migrate

db = SQLAlchemy()
cors = CORS()
admin = Admin(template_mode="bootstrap3")
migrate = Migrate()


def create_app():

    # Instantiate the app
    app = Flask(__name__)

    # Set config
    app.config['SECRET_KEY'] = 'determination'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Setup extensions
    db.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}})
    admin.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from .views import main
    app.register_blueprint(main)

    # Shell context for flask cli
    @app.shell_context_processor
    def context():
        return {"app": app, "db": db}

    return app
