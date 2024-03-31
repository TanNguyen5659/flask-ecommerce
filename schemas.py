from marshmallow import Schema, fields

class PostSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str()
    body = fields.Str(required=True)
    user_id = fields.Int(required=True)

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)
    first_name= fields.Str()
    last_name= fields.Str()

class PostWithUserSchema(PostSchema):
    author = fields.Nested(UserSchema)

class UserWithPostsSchema(UserSchema):
    posts = fields.List(fields.Nested(PostSchema), dump_only = True)
