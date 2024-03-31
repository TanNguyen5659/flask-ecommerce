from datetime import datetime

from app import db

class PostModel(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    author = db.relationship("UserModel", back_populates='posts')

    def from_dict(self, a_dict):
        self.title = a_dict['title']
        setattr(self, 'body', a_dict['body'])
        setattr(self, 'user_id', int(a_dict['user_id'] ))

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def del_post(self):
        db.session.delete(self)
        db.session.commit()

    