import os
import json
from datetime import timedelta
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from users.api import UserRestApi
from users.model import User

def create_app(custom_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    config_file = os.environ.get("CONF_FILE", "../config.json")
    app.config.from_file(config_file, load=json.load)

    # JWT Configuration
    jwt = JWTManager(app)

    # Add all routes contained in <Class>RestApi
    app.register_blueprint(UserRestApi().get_blueprint())
    # CORS config
    CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Auth: Login Route (Generate JWT)
    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        if not data or not data.get('name') or not data.get('password'):
            return jsonify({"error": "Missing username or password"}), 400
        user = User.query.filter_by(name = data['name']).first()
        # TODO use bcrypt.check_password_hash instead
        if user and user.password == data['password']:

            access_token = create_access_token(identity=user.name, expires_delta=timedelta(seconds=15))
            refresh_token = create_refresh_token(identity=user.name, expires_delta=timedelta(hours=24))

            return jsonify({
                "access_token":access_token,
                "refresh_token": refresh_token,
                "user_details": user.to_dict()
                }), 200

        return jsonify({"error": "Invalid credentials"}), 401

    @app.route("/refresh", methods=["POST"])
    @jwt_required(refresh=True)
    def refresh():
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user, expires_delta=timedelta(seconds=15))
        return jsonify(access_token=new_access_token)

    if not app.config['TESTING']:
        @app.before_request
        def check_authentication():
            # exclude /login and public endpoints from this check
            excluded_paths = ["/login", "/refresh"]
            if any(request.path.startswith(p) for p in excluded_paths):
                return None

            # Use Flask-JWT-Extended to handle authentication
            try:
                jwt_required()(lambda: None)()
            except Exception as e:
                return jsonify({"message": "Authentication Token is missing or invalid!", "error": str(e)}), 401

    return app
