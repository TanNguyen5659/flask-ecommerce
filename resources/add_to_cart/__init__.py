from flask_smorest import Blueprint

bp = Blueprint("like_post", __name__, description="Routes for Post Likes")

from . import routes