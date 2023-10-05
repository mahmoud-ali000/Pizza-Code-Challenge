from api import db, api
from flask import make_response, jsonify,request
from flask_restful import Resource,reqparse 
from .models import Restaurant
from .models import Pizza
from .models import RestaurantPizza
from datetime import datetime

class HomeResource(Resource):
    def get(self):
        return "Restaurant Pizza api"
api.add_resource(HomeResource,'/')

class PizzaResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizzas_dict =  [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients } for pizza in pizzas ]
        response = make_response(jsonify(pizzas_dict), 200)
        return response

# Define the routes and associated resources
class RestaurantsResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurants_dict = []
        for r in restaurants:
            restaurant_dict = {"id":r.id, "name": r.name, "address": r.address}
            restaurants_dict.append(restaurant_dict)
        response = make_response(jsonify(restaurants_dict), 200)
        return response
    
class RestaurantByIdResource(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            pizzas =  [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients } for pizza in restaurant.pizzas ]
            restaurant_dict = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": pizzas
