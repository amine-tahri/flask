# 1 recieve API payload
# 2 validate schema
# 3 call command function
from flask import request, jsonify
from flask_appbuilder.api import BaseApi as FabBaseApi, expose
from articles.schemas import ArticleSchema, ArticlePosPuttSchema
from articles.commands.create import CreateArticleCommand
from articles.dao import ArticleDAO


class ArticleRestApi(FabBaseApi):
    route_base = "/articles"
    model_DAO = ArticleDAO
    model_get_schema= ArticleSchema()
    model_get_all_schema= ArticleSchema(many=True)
    model_post_schema = ArticlePosPuttSchema()
    model_put_schema = ArticlePosPuttSchema()
    create_command = CreateArticleCommand

    @expose('/', methods=['GET'])
    def get_all(self):
        try:
            model_list = self.model_DAO.get_all()
            result = self.model_get_all_schema.dump(model_list)
            return jsonify(result)
        except Exception as e:
            return self.response_500
    
    @expose('/<int:id>', methods=['GET'])
    def get_by_id(self, id):
        try:
            model = self.model_DAO.get_by_id(id)
            if not model:
                return self.no_item_found_response(id)
            result = self.model_get_schema.dump(model)
            return jsonify(result)
        except Exception as e:
            return self.response_500

    @expose('/', methods=['POST'])
    def create(self):
        try:
            item = self.model_post_schema.load(request.json)
            new_model = self.create_command(item).run()
            result = self.model_get_schema.dump(new_model)
            return jsonify(result)
        except Exception as e:
            return self.response_500

    def no_item_found_response(self, id_not_found):
        message = 'No item found with the given id: {id_not_found}'.format(id_not_found=id_not_found)
        return jsonify(message), 404