from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from Config import Config

app = Flask(__name__)

app.config.from_object(Config)
api = Api(app)
jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user_model import UserModel
from models.product_model import ProductModel
from models.add_to_cart_model import AddToModel

from resources.product import bp as product_bp
app.register_blueprint(product_bp)
from resources.user import bp as user_bp
app.register_blueprint(user_bp)
from resources.add_to_cart import bp as add_to_cart_bp
app.register_blueprint(add_to_cart_bp)

