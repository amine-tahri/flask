# import ...
from users.dao import UserDAO

class CreateUserCommand():
    def __init__(self, data):
        self._properties = data.copy()

    def run(self):
        self.validate()
        user = UserDAO.create(self._properties)
        return user
        # execution logic code
        # call DAO code

    def validate(self):
        # validation code
        pass
