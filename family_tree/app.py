from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from family_tree import config
import flask_cors

from family_tree.views import health_check

cors = flask_cors.CORS()


def create_app():
    app = Flask(__name__)
    print("app")
    cors.init_app(app)
    app.register_blueprint(health_check.blueprint, url_prefix='/api')
    engine = create_engine("postgres://{}:{}@localhost:5432".format(config.USER, config.PASSWORD))
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return app
