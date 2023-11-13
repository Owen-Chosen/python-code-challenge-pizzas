#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/restaurants')
def restaurants():
    all_restaurants = []
    for restaurant in Restaurant.query.all():
        all_restaurants.append(restaurant.to_dict())
    return make_response(jsonify(all_restaurants), 200)

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurants_by_id(id):
    restaurant = Restaurant.query.filter_by(id=id).first()
    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)
    else:
        if request.method=='GET':
            return make_response(jsonify(restaurant.to_dict()), 200)
        elif request.method=='DELETE':
            db.session.delete(restaurant)
            db.session.commit()
        return make_response(jsonify({}), 200)
    
@app.route('/pizzas')
def pizzas():
    all_pizzas = []
    for pizza in Pizza.query.all():
        all_pizzas.append(pizza.to_dict())
    return make_response(jsonify(all_pizzas), 200)

@app.route('/restaurant_pizzas', methods=['GET', 'POST'])
def restaurant_pizzas():
    all_restaurant_pizzas = RestaurantPizza.query.all()

    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
