from typing import Optional
from flask import jsonify, Blueprint, Response
from marshmallow import Schema
from marshmallow import ValidationError
from backend.common.base_dao import BaseDAO


def expose(url: str = "/", methods: list[str] = ["GET"]):
    def wrap(f):
        if not hasattr(f, "_urls"):
            f._urls = []
        f._urls.append((url, methods))
        return f
    return wrap

class BaseApi():
    route_base = ""
    model_DAO: Optional[BaseDAO] = None
    model_get_schema: Optional[Schema] = None
    model_get_all_schema: Optional[Schema] = None
    model_post_schema: Optional[Schema] = None
    model_put_schema: Optional[Schema] = None
    update_command = None
    create_command = None
    use_pagination = False
    read_only = False

    def __init__(self) -> None:
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

    @expose('/<int:id>', methods=['GET'])
    def get_by_id(self, id):
        try:
            pass
        except Exception as e:
            return self.response_500()

    @expose('/', methods=['GET'])
    def get_all(self):
        try:
            pass
        except Exception as e:
            return self.response_500()

    @expose('/<int:id>', methods=['PUT'])
    def update(self, id):
        if self.read_only:
            return self.response_405()
        try:
            pass
        except ValidationError as error:
            pass
        try:
            pass
        # except IdNotFoundException:
            # pass
        except ValidationError as e2:
            pass
        # except ConflictException as error:
            # pass
        except Exception as e:
            pass

    @expose('/', methods=['POST'])
    def create(self):
        if self.read_only:
            return self.response_405()
        try:
            pass
        # Validates schema
        except ValidationError as error:
            pass
        try:
            pass
        except ValidationError as err:
            pass
        # except ConflictException as error:
            # pass
        except Exception as e:
            pass

    # TODO add other error handler

    @expose('/nombre', methods=['GET'])
    def get_count(self):
        try:
            pass
        except Exception as e:
            pass

    def response(self, status_code, **kwargs):
        return Response(status=status_code, **kwargs)

    def response_error(self, status_code, message):
        return jsonify({
            "message": message
        }), status_code

    def response_400(self, message = "Bad Request"):
        return self.response_error(400, message)

    def response_403(self, message = "Forbidden"):
        return self.response_error(403, message)

    def response_404(self, message = "Not found"):
        return self.response_error(404, message)

    def response_405(self, message = "Method not allowed"):
        return self.response_error(405, message)

    def response_409(self, message = "Conflict"):
        return self.response_error(409, message)

    def response_500(self, message = "Internal Server Error"):
        return self.response_error(500, message)

    def no_item_found_response(self, id_not_found):
        return self.response_404('No item found with the given id: %(id_not_found)s', id_not_found=id_not_found)