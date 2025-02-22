import os
import json
from flask import Flask
from flask_cors import CORS
from users.api import UserRestApi

def create_app(custom_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    config_file = os.environ.get("CONF_FILE", "../config.json")
    app.config.from_file(config_file, load=json.load)

    # Add all routes contained in <Class>RestApi
    app.register_blueprint(UserRestApi().get_blueprint())
    print(app.config)
    # CORS config
    CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
    app.config['CORS_HEADERS'] = 'Content-Type'

    return app
