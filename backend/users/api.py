# 1 recieve API payload
# 2 validate schema
# 3 call command function
from flask import request, jsonify
from flask import Blueprint

from users.schemas import UserSchema, UserPosPutSchema
from users.dao import UserDAO

from users.commands.create import CreateUserCommand
from users.commands.update import UpdateUserCommand

def expose(url: str = "/", methods: list[str] = ["GET"]): # pylint: disable=dangerous-default-value
    def wrap(f):
        if not hasattr(f, "_urls"):
            f._urls = []
        f._urls.append((url, methods))
        return f
    return wrap

class UserRestApi():
    route_base = "/users"
    model_DAO = UserDAO
    model_get_schema= UserSchema()
    model_get_all_schema= UserSchema(many=True)
    model_post_schema = UserPosPutSchema()
    model_put_schema = UserPosPutSchema()
    create_command = CreateUserCommand
    update_command = UpdateUserCommand

    def __init__(self):
        self.name = type(self).__name__

    def get_blueprint(self):
        self.blueprint = Blueprint(
            self.name,
            self.name,
            url_prefix=self.route_base
        )
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            for url in getattr(attr, "_urls", ()):
                self.blueprint.add_url_rule(url[0], view_func=attr, methods=url[1])
        return self.blueprint

    @expose('/', methods=['GET'])
    def get_all(self):
        try:
            model_list = self.model_DAO.get_all()
            result = self.model_get_all_schema.dump(model_list)
            return jsonify(result)
        except Exception as e:
            return str(e)
    
    @expose('/<int:id>', methods=['GET'])
    def get_by_id(self, id):
        try:
            model = self.model_DAO.get_by_id(id)
            if not model:
                return self.no_item_found_response(id)
            return jsonify(self.model_get_schema.dump(model))
        except Exception as e:
            return self.response_500()

    @expose('/', methods=['POST'])
    def create(self):
        try:
            item = self.model_post_schema.load(request.json)
            new_model = self.create_command(item).run()
            print('new_model')
            result = self.model_get_schema.dump(new_model)
            return jsonify(result)
        except Exception as e:
            return str(e)

    @expose('/<id>', methods=['PUT'])
    def update(self, id):
        try:
            item = self.model_put_schema.load(request.json)
            updated_model = self.update_command(id, item).run()
            result = self.model_get_schema.dump(updated_model)
            return jsonify(result)
        except Exception as e:
            return self.response_500()

    def no_item_found_response(self, id_not_found):
        message = 'No item found with the given id: {id_not_found}'.format(id_not_found=id_not_found)
        return jsonify(message), 404