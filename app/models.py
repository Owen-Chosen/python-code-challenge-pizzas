from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

#-------------------------------------------------------------------------------------
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurants',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ingredients = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    restaurants = db.relationship('RestaurantPizza', back_populates='pizza')

    def __repr__(self):
        return f'<Pizza {self.name}, {self.ingredients}>'

#-------------------------------------------------------------------------------------
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(500))
    pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

    def __repr__(self):
        return f'<Restaurant {self.name},{self.address}>'
    
#-------------------------------------------------------------------------------------
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    serialize_rules = ('-pizza', 'restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    pizza = db.relationship('Pizza', back_populates = 'restaurants')
    restaurant = db.relationship('Restaurant', back_populates = 'pizzas')

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('price')
    def validate_price(self, key, price):
        if price<1 or price>30:
            raise ValueError('Price must be between 1 and 30')
        return price

    def __repr__(self):
        return f'<Pizza {self.pizza}, {self.restaurant}>'