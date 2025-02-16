# interact with DB (example : db.session.add(model))
from users.model import User

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()
class UserDAO():
    model_cls = User

    @staticmethod
    def get_all(**kwargs):
        query = db.session.query(UserDAO.model_cls)
        return query.all()

    @staticmethod
    def get_by_id(model_id, **kwargs):
        query = db.session.get(UserDAO.model_cls, model_id)
        return query

    @classmethod
    def create(cls, properties, commit = True, **kwargs):
        model = cls.model_cls()

        for key, value in properties.items():
            if not isinstance(value, dict):
                setattr(model, key, value)
        try:
            db.session.add(model)
            # TODO commit ??
            if commit:
                db.session.commit()
        except SQLAlchemyError as ex:
            db.session.rollback()
        return model

    @classmethod
    def update(cls, model, properties, commit = True, **kwargs):
        for key, value in properties.items():
            if not isinstance(value, dict):
                setattr(model, key, value)
        try:
            db.session.merge(model)
            # TODO commit ??
            if commit:
                db.session.commit()
        except SQLAlchemyError as ex:
            db.session.rollback()
        return model
