# import ...
from users.model import User
from users.dao import UserDAO
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError

class UpdateUserCommand():
    def __init__(self, model_id, data):
        self._model_id = model_id
        self._properties = data.copy()
        self._model = User

    def run(self):
        self.validate()
        user = UserDAO.update(self._model, self._properties)
        return user
        # execution logic code
        # call DAO code

    def validate(self):
        # validation code
        self._model = UserDAO.get_by_id(self._model_id)
        if not self._model:
            raise ValidationError("Item Not Found")