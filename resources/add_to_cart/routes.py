from flask.views import MethodView
from flask_smorest import abort

from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user_model import UserModel

from . import bp
from models.add_to_cart_model import AddToModel 
from models.product_model import ProductModel
from schemas import ProductSchema, UserSchema


@bp.route('/like-post/<product_id>')
class AddItem(MethodView):

    @jwt_required()
    @bp.response(201, ProductSchema)
    def post(self, product_id):

        user_id = get_jwt_identity()
        product = ProductModel.query.get(product_id)
        user = UserModel.query.get(user_id)
        if user and product:
            added = AddToModel.query.filter_by(product_id = product_id).filter_by(user_id = user_id).all()
            if added:
                return product
            addToModel = AddToModel(user_id=user_id, product_id=product_id)
            addToModel.save()
            return product
        abort(400, message="Invalid User or Product")

    @jwt_required()
    def delete(self, product_id):
        user_id = get_jwt_identity()
        product = ProductModel.query.get(product_id)
        user = UserModel.query.get(user_id)
        if user and product:
            added = AddToModel.query.filter_by(product_id = product_id).filter_by(user_id = user_id).all()
            
            for like in added:
                like.delete()

            return {'message':"deleted"}, 201
        abort(400, message="Invalid User or Product")


    @bp.response(200, UserSchema(many=True))
    def get(self, product_id):
        product = ProductModel.query.get(product_id)
        if not product:
            abort(400, message="Invalid Product")

        items = AddToModel.query.filter_by(product_id = product_id).all()

        return [UserModel.query.get(like.user_id) for item in items]    

# @bp.route('/view-cart/<user_id>')
# class ViewCart(MethodView):
#     @bp.response(200, ProductSchema(many=True))
#     def get(self, user_id):
#         user = UserModel.query.get(user_id)
#         if not user:
#             abort(400, message="Invalid User")

#         likes = AddToModel.query.filter_by(user_id = user_id).all()

#         return [ProductModel.query.get(like.product_id) for like in likes] 
    
@bp.route('/view-cart/<user_id>')
class ViewCart(MethodView):
    @bp.response(200, ProductSchema(many=True))
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if not user:
            abort(400, message="Invalid User")

        items = AddToModel.query.filter_by(user_id=user_id).all()
        print(f"Number of likes retrieved: {len(items)}")
        products = [ProductModel.query.get(item.product_id) for item in items]
        print(f"Number of products retrieved: {len(products)}")
        total = len(products)
        print(f"Total calculated: {total}")


        # Combine products and total into a dictionary for consistent response format
        response_data = {'products': products, 'total': total}
        return response_data
