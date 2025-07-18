from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    password = fields.Str(required=True)

class UserPosPutSchema(Schema):
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    password = fields.Str(required=True)
