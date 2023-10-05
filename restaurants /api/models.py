from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255))
    pizzas = db.relationship("Pizza",secondary = "restaurant_pizzas",back_populates="restaurants")

    @validates("name")
    def validate_name(self, key, name):
        if not len(name.strip().split(" ")) < 50:
            raise ValueError("Name less than 50 words in length")
        restaurant = Restaurant.query.filter_by(name=name).first()
        if restaurant:
            raise ValueError("Value must be unique")
        return name
    

    def __str__(self):
        return self.name
    
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255))
    created_at =db.Column(db.DateTime,default = datetime.utcnow)
    update_at = db.Column(db.DateTime,default = datetime.utcnow)
    restaurants = db.relationship("Restaurant",secondary = "restaurant_pizzas",back_populates="pizzas")

    def __str__(self):
        return self.name

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
