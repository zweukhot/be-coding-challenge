from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from family_tree import config
import flask_cors

from family_tree.views import family

cors = flask_cors.CORS()


def create_app():
    app = Flask(__name__)
    cors.init_app(app)
    app.register_blueprint(family.blueprint, url_prefix='/api')
    database_file = "postgres://{}:{}@localhost:5432".format(config.USER, config.PASSWORD)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_file
    db = SQLAlchemy(app)
    app.db = db
    return app
