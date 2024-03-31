from app import db

class AddToModel(db.Model):

    __tablename__ = 'add_to'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable= False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
