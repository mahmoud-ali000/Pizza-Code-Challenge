#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from api import app
from api.models import db, Pizza, Restaurant, RestaurantPizza

fake = Faker()

with app.app_context():
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    pizzas = []
    for i in range(10):
        p = Pizza(name=fake.name(), ingredients=fake.word())
        pizzas.append(p)

    db.session.add_all(pizzas)

    restaurants = []
    for i in range(10):
        r = Restaurant(name=fake.company(), address=fake.address())
        restaurants.append(r)

    db.session.add_all(restaurants)

    restaurant_pizzas = []
    for i in range(20):
        rp = RestaurantPizza(
            price=randint(1, 30), pizza_id=randint(1, 10), restaurant_id=randint(1, 10)
        )
        restaurant_pizzas.append(rp)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()
