from datetime import datetime

from app import db

class ProductModel(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    price = db.Column(db.Integer, nullable = False)
    # timestamp = db.Column(db.DateTime, default = datetime.utcnow)

    def from_dict(self, a_dict):
        self.name = a_dict['name']
        setattr(self, 'price', a_dict['price'])
        

    def save_product(self):
        db.session.add(self)
        db.session.commit()

    def del_product(self):
        db.session.delete(self)
        db.session.commit()

    