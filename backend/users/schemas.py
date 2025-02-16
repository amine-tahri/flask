from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    age = fields.Int(required=True)
    sexe = fields.Str(required=True)

class UserPosPutSchema(Schema):
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    age = fields.Int(required=True)
    sexe = fields.Str(required=True)
