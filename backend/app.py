from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_appbuilder.api import expose
from flask_cors import CORS
from marshmallow import Schema, fields
from flask_appbuilder import SQLA, AppBuilder, ModelView

from users.model import User
from users.api import UserRestApi
from articles.api import ArticleRestApi
# from users.schemas import UserSchema

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configuration settings
app.config['SECRET_KEY'] = 'dev_secret_key'  # Used for signing tokens
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/opide_2'

# db = SQLAlchemy(app)
# jwt = JWTManager(app)

db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

db.create_all()

appbuilder.add_api(UserRestApi)
appbuilder.add_api(ArticleRestApi)

# # Model for Article
# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.String(500), nullable=False)

# # Serialization schema for Article
# class ArticleSchema(Schema):
#     id = fields.Int()
#     title = fields.Str(required=True)
#     content = fields.Str(required=True)

# class UserSchema(Schema):
#     id = fields.Int()
#     name = fields.Str(required=True)
#     address = fields.Str(required=True)
#     age = fields.Int(required=True)
#     sexe = fields.Str(required=True)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     address = db.Column(db.String(200), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     sexe = db.Column(db.String(10), nullable=False)

# article_schema = ArticleSchema()
# articles_schema = ArticleSchema(many=True)

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

# # User routes
# @expose('/users', methods=['POST'])
# def add_user():
#     user_data = user_schema.load(request.json)
#     new_user = User(**user_data)
#     db.session.add(new_user)
#     db.session.commit()
#     return user_schema.dump(new_user), 201

# @expose('/users', methods=['GET'])
# # @jwt_required()  # Uncomment if you want to secure this route
# def get_users():
#     users = User.query.all()
#     return jsonify(users_schema.dump(users))

# # Article routes
# @expose('/articles', methods=['GET'])
# def get_articles():
#     articles = Article.query.all()
#     return jsonify(articles_schema.dump(articles))

# @expose('/articles', methods=['POST'])
# def add_article():
#     article_data = article_schema.load(request.json)
#     new_article = Article(**article_data)
#     db.session.add(new_article)
#     db.session.commit()
#     return article_schema.dump(new_article), 201

# @expose('/articles/<int:id>', methods=['PUT'])
# def update_article(id):
#     article = Article.query.get(id)
#     if not article:
#         return jsonify({"message": "Article not found"}), 404

#     for key, value in request.json.items():
#         if hasattr(article, key):
#             setattr(article, key, value)
#     db.session.commit()
#     return article_schema.dump(article), 200

# @expose('/users/<int:id>', methods=['PUT'])
# def update_user(id):
#     user = User.query.get(id)
#     if not user:
#         return jsonify({"message": "User not found"}), 404

#     for key, value in request.json.items():
#         if hasattr(user, key):
#             setattr(user, key, value)
#     db.session.commit()
#     return user_schema.dump(user), 200

if __name__ == '__main__':
    app.run(debug=True)