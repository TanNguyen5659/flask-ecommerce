from flask.views import MethodView
from flask_smorest import abort

from flask_jwt_extended import jwt_required

from . import bp
from schemas import ProductSchema
from models.product_model import ProductModel

@bp.route('/product')
class ProductList(MethodView):
    
    @bp.response(201, ProductSchema)
    @bp.arguments(ProductSchema)
    def post(self, product_data):

        try:
            product = ProductModel()
            product.from_dict(product_data)

            product.save_product()

            return product
        except:
            abort(400, message=f"{product.name} failed to product")

    @bp.response(200, ProductSchema(many=True))
    def get(self):
        return ProductModel.query.all()

@bp.route('/product/<product_id>')
class Product(MethodView):

    @bp.response(200, ProductSchema)
    def get(self, product_id):
        try: 
            return ProductModel.query.get(product_id)
        except:
            abort(400, message="Product not found")

    # @bp.arguments(ProductSchema)
    # @bp.response(201, ProductSchema)
    # def put(self, product_data, product_id):
            
    #     print(product_data)
    #     product = ProductModel.query.get(product_id)
    #     if not product:
    #         abort(400, message="product not found")

    #     if product_data['user_id'] == product.user_id:
    #         og_user_id = product.user_id
    #         product.from_dict(product_data)
    #         product.user_id = og_user_id

    #         product.save_product()
    #         return product

    def delete(self, product_id):

        product = ProductModel.query.get(product_id)
        if not product:
            abort(400, message="product not found")
        
        product.del_product()
        return {'message': f'product: {product_id} deleted'}, 200

