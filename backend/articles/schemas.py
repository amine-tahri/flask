from marshmallow import Schema, fields

class ArticleSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    content = fields.Str(required=True)

class ArticlePosPuttSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)
