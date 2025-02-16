# interact with DB (example : db.session.add(model))
from articles.model import Article

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class ArticleDAO():
    model_cls = Article

    @staticmethod
    def get_all(**kwargs):
        query = db.session.query(ArticleDAO.model_cls)
        return query.all()

    @staticmethod
    def get_by_id(model_id, **kwargs):
        query = db.session.get(ArticleDAO.model_cls, model_id)
        return query

    @staticmethod
    def create(properties, commit: True):
        pass
