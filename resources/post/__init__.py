from flask_smorest import Blueprint

bp = Blueprint("posts", __name__, description="Routes for Posts")

from . import routes