from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)