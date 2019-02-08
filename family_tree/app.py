from flask import Flask
import flask_cors

from family_tree import config
from family_tree.views import health_check

cors = flask_cors.CORS()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    cors.init_app(app)
    app.register_blueprint(health_check.blueprint, url_prefix='/api')

    return app
