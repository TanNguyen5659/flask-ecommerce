from app import db

class LikePostModel(db.Model):

    __tablename__ = 'like_post'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable= False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
