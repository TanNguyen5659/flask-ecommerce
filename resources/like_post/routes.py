from flask.views import MethodView
from flask_smorest import abort

from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user_model import UserModel

from . import bp
from models.like_post_model import LikePostModel 
from models.post_model import PostModel
from schemas import PostSchema, UserSchema


@bp.route('/like-post/<post_id>')
class LikePost(MethodView):

    @jwt_required()
    @bp.response(201, PostSchema)
    def post(self, post_id):

        user_id = get_jwt_identity()
        post = PostModel.query.get(post_id)
        user = UserModel.query.get(user_id)
        if user and post:
            liked_by_user = LikePostModel.query.filter_by(post_id = post_id).filter_by(user_id = user_id).all()
            if liked_by_user:
                return post
            likePostModel = LikePostModel(user_id=user_id, post_id=post_id)
            likePostModel.save()
            return post
        abort(400, message="Invalid User or Post")

    @jwt_required()
    def delete(self, post_id):
        user_id = get_jwt_identity()
        post = PostModel.query.get(post_id)
        user = UserModel.query.get(user_id)
        if user and post:
            liked_by_user = LikePostModel.query.filter_by(post_id = post_id).filter_by(user_id = user_id).all()
            
            for like in liked_by_user:
                like.delete()

            return {'message':"deleted"}, 201
        abort(400, message="Invalid User or Post")


    @bp.response(200, UserSchema(many=True))
    def get(self, post_id):
        post = PostModel.query.get(post_id)
        if not post:
            abort(400, message="Invalid Post")

        likes = LikePostModel.query.filter_by(post_id = post_id).all()

        return [UserModel.query.get(like.user_id) for like in likes]    