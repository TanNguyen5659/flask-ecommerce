from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    price = fields.Int(required=True)


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)
    first_name= fields.Str()
    last_name= fields.Str()

