from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    rooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.String(20))
    location = db.Column(db.String(50))
    propType = db.Column(db.String(20))
    photo = db.Column(db.String(120))
        
    def __init__(self, title, description, rooms, bathrooms, price, location, propType, photo):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.location = location
        self.propType = propType
        self.photo = photo


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' %  self.id