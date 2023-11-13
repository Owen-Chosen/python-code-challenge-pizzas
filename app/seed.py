from faker import Faker

from models import db, Restaurant, Pizza, RestaurantPizza
from app import app
from random import randint, choices, choice as rc

fake = Faker()

pizza_name = [
    "Chessy Chicken",
    "Chicken BBQ",
    "Margherita",
    "Mexican Beef",
    "Chesseburger",
    "Meaty BBQ",
    "Pepperoni",
    "Super Meaty",
    "Veggie Overlaod",
    "Dodo Supreme"
]

pizza_ingredient = [
    "Cheese",
    "Plantain",
    "Beef",
    "Chili",
    "Suya",
    "Veggie",
    "Chicken",
    "Shawarma",
    "Tomatoes",
    "Red Pepper",
    "Broccoli",
    "Roasted Fennel",
    "Cauliflower",
    "Mushrooms",
    "Grilled Eggplant",
    "Grilled Pineapple",
    "Garlic",
    "Onions",
    "Jalapeños",
    "Capers",
    "Cashew Cream",
    "Balsamic Glaze"
]


with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
    restaurant_objects = []
    for i in range(10):
        new_rest = Restaurant( name = fake.company(), address = fake.address() )
        db.session.add( new_rest )
        restaurant_objects.append( new_rest )
    # print(restaurant_objects)
    db.session.commit()


    pizza_objects = []
    for i in range(10):
        new_pizza = Pizza( name = pizza_name[i], ingredients = ', '.join(choices(pizza_ingredient, k=randint(3, 5))) )
        db.session.add( new_pizza )
        pizza_objects.append( new_pizza )
    # print(pizza_objects)
    db.session.commit()


    restaurant_pizza_objects = []
    for i in range(10):
        new_restaurant_pizza = RestaurantPizza(price = randint(1, 30), pizza=rc(pizza_objects), restaurant=rc(restaurant_objects))
        db.session.add( new_restaurant_pizza )
        restaurant_pizza_objects.append( new_restaurant_pizza )
    # print(restaurant_pizza_objects)
    db.session.commit()

    # rest = Restaurant.query.filter(Restaurant.id==2).first()
    # print(rest.pizzas)